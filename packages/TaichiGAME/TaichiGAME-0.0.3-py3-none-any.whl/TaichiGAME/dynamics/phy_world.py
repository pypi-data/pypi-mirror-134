from typing import Optional, Union, List

from ..math.matrix import Matrix
from ..dynamics.body import Body
from ..common.random import RandomGenerator
from .joint.joint import Joint
from .joint.distance import DistanceJoint, DistanceJointPrimitive
from .joint.point import PointJoint, PointJointPrimitive
from .joint.pulley import PulleyJoint, PulleyJointPrimitive
from .joint.revolute import RevoluteJoint, RevoluteJointPrimitive
from .joint.rotation import OrientationJoint, OrientationJointPrimitive
from .joint.rotation import RotationJointPrimitive, RotationJoint


class PhysicsWorld():
    def __init__(self):
        self._gravity: Matrix = Matrix([0.0, -1.0], 'vec')
        self._linear_vel_damping: float = 0.9
        self._ang_vel_damping: float = 0.9
        self._linear_vel_threshold: float = 0.02
        self._ang_vel_threshold: float = 0.02
        self._air_fric_coeff: float = 0.7

        self._bias: float = 0.8
        self._vel_iter: int = 1
        self._pos_iter: int = 1

        self._grav_ena: bool = True
        self._damping_ena: bool = True
        self._body_list: List[Body] = []
        self._joint_list: List[Joint] = []

    def prepare_velocity_constraint(self, dt: float) -> None:
        for joint in self._joint_list:
            if joint.active:
                joint.prepare(dt)

    def step_velocity(self, dt: float) -> None:
        g: Matrix = self._gravity if self._grav_ena else Matrix([0.0, 0.0],
                                                                'vec')
        lvd: float = 1.0
        avd: float = 1.0

        if self._damping_ena:
            lvd = 1.0 / (1.0 + dt * self._linear_vel_damping)
            avd = 1.0 / (1.0 + dt * self._ang_vel_damping)

        for body in self._body_list:
            if body.type == Body.Type.Static:
                body.vel.clear()
                body.ang_vel = 0.0

            elif body.type == Body.Type.Dynamic:
                body.forces += g * body.mass
                # NOTE: meet the operator overload seq
                body.vel += body.forces * dt * body.inv_mass
                body.ang_vel += body.inv_inertia * body.torques * dt

                body.vel *= lvd
                body.ang_vel *= avd

            elif body.type == Body.Type.Kinematic:
                # NOTE: meet the operator overload seq
                body.vel += body.forces * dt * body.inv_mass
                body.ang_vel += body.inv_inertia * body.torques * dt

                body.vel *= lvd
                body.ang_vel *= avd

            elif body.type == Body.Type.Bullet:
                pass

    def solve_velocity_constraint(self, dt: float) -> None:
        for joint in self._joint_list:
            if joint.active:
                joint.solve_velocity(dt)

    def step_position(self, dt: float) -> None:
        for body in self._body_list:
            if body.type == Body.Type.Static:
                pass
            elif body.type == Body.Type.Dynamic:
                body.pos += body.vel * dt
                body.rot += body.ang_vel * dt
                body.forces.clear()
                body.clear_torque()

            elif body.type == Body.Type.Kinematic:
                body.pos += body.vel * dt
                body.rot += body.ang_vel * dt
                body.forces.clear()
                body.clear_torque()

            elif body.type == Body.Type.Bullet:
                pass

    def solve_position_constraint(self, dt: float) -> None:
        for joint in self._joint_list:
            if joint.active:
                joint.solve_position(dt)

    @property
    def grav(self) -> Matrix:
        return self._gravity

    @grav.setter
    def grav(self, grav: Matrix) -> None:
        self._gravity = grav

    @property
    def lin_vel_damping(self) -> float:
        return self._linear_vel_damping

    @lin_vel_damping.setter
    def lin_vel_damping(self, lin_vel_damping: float) -> None:
        self._linear_vel_damping = lin_vel_damping

    @property
    def ang_vel_damping(self) -> float:
        return self._ang_vel_damping

    @ang_vel_damping.setter
    def ang_vel_damping(self, ang_vel_damping: float) -> None:
        self._ang_vel_damping = ang_vel_damping

    @property
    def lin_vel_thold(self) -> float:
        return self._linear_vel_threshold

    @lin_vel_thold.setter
    def lin_vel_thold(self, lin_vel_thold: float) -> None:
        self._linear_vel_threshold = lin_vel_thold

    @property
    def ang_vel_thold(self) -> float:
        return self._ang_vel_threshold

    @ang_vel_thold.setter
    def ang_vel_thold(self, ang_vel_thold: float) -> None:
        self._ang_vel_threshold = ang_vel_thold

    @property
    def air_fric_coeff(self) -> float:
        return self._air_fric_coeff

    @air_fric_coeff.setter
    def air_fric_coeff(self, air_fric_coeff: float) -> None:
        self._air_fric_coeff = air_fric_coeff

    @property
    def bias(self) -> float:
        return self._bias

    @bias.setter
    def bias(self, bias: float) -> None:
        self._bias = bias

    @property
    def vel_iter(self) -> int:
        return self._vel_iter

    @vel_iter.setter
    def vel_iter(self, vel_iter: int) -> None:
        self._vel_iter = vel_iter

    @property
    def pos_iter(self) -> int:
        return self._pos_iter

    @pos_iter.setter
    def pos_iter(self, pos_iter: int) -> None:
        self._pos_iter = pos_iter

    @property
    def grav_ena(self) -> bool:
        return self._grav_ena

    @grav_ena.setter
    def grav_ena(self, grav_ena: bool) -> None:
        self._grav_ena = grav_ena

    @property
    def damping_ena(self) -> bool:
        return self._damping_ena

    @damping_ena.setter
    def damping_ena(self, damping_ena: bool) -> None:
        self._damping_ena = damping_ena

    def create_body(self) -> Body:
        body: Body = Body()
        body.id = RandomGenerator.unique()
        self._body_list.append(body)
        return body

    def create_joint(
        self, prim: Union[RotationJointPrimitive, PointJointPrimitive,
                          DistanceJointPrimitive, PulleyJointPrimitive,
                          RevoluteJointPrimitive, OrientationJointPrimitive]
    ) -> Union[RotationJoint, PointJoint, DistanceJoint, PulleyJoint,
               RevoluteJoint, OrientationJoint]:

        joint: Optional[Union[RotationJoint, PointJoint, DistanceJoint,
                              PulleyJoint, RevoluteJoint,
                              OrientationJoint]] = None

        if isinstance(prim, RotationJointPrimitive):
            joint = RotationJoint(prim)
        elif isinstance(prim, PointJointPrimitive):
            joint = PointJoint(prim)
        elif isinstance(prim, DistanceJointPrimitive):
            joint = DistanceJoint(prim)
        elif isinstance(prim, PulleyJointPrimitive):
            joint = PulleyJoint(prim)
        elif isinstance(prim, RevoluteJointPrimitive):
            joint = RevoluteJoint(prim)
        elif isinstance(prim, OrientationJointPrimitive):
            joint = OrientationJoint(prim)

        joint.id = RandomGenerator.unique()
        self._joint_list.append(joint)
        return joint

    def remove_body(self, body: Body) -> None:
        for b in self._body_list:
            if body == b:
                RandomGenerator.pop(body.id)
                self._body_list.remove(body)
                break

    def remove_joint(self, joint: Joint) -> None:
        for j in self._joint_list:
            if joint == j:
                RandomGenerator.pop(joint.id)
                self._joint_list.remove(joint)

    def clear_all_bodies(self) -> None:
        self._body_list.clear()

    def clear_all_joints(self) -> None:
        self._joint_list.clear()
