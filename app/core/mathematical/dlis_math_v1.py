
from dataclasses import dataclass
import math


EPSILON=1e-12


@dataclass
class DLISState:

    entropy: float

    divergence: float

    resilience: float

    psi: float

    pi: float

    omega: float

    sigma: float

    phi: float

    kappa: float

    lambda_index: float


class DLISMath:

    VERSION="8.1"


    def psi(

        self,

        H,

        D,

        R

    ):

        return (H*D)/(R+EPSILON)


    def pi(

        self,

        psi,

        D

    ):

        return psi*D


    def omega(

        self,

        R,

        psi

    ):

        return R/(1.0+psi)


    def sigma(

        self,

        omega,

        pi

    ):

        return omega-pi


    def phi(

        self,

        psi,

        pi

    ):

        return math.sqrt(

            psi**2+

            pi**2

        )


    def kappa(

        self,

        psi,

        omega

    ):

        return psi-omega


    def collapse(

        self,

        psi

    ):

        return 1-math.exp(-psi)


    def evaluate(

        self,

        H,

        D,

        R

    ):

        PSI=self.psi(

            H,

            D,

            R

        )

        PI=self.pi(

            PSI,

            D

        )

        OMEGA=self.omega(

            R,

            PSI

        )

        SIGMA=self.sigma(

            OMEGA,

            PI

        )

        PHI=self.phi(

            PSI,

            PI

        )

        KAPPA=self.kappa(

            PSI,

            OMEGA

        )

        LAMBDA=self.collapse(

            PSI

        )

        return DLISState(

            entropy=H,

            divergence=D,

            resilience=R,

            psi=PSI,

            pi=PI,

            omega=OMEGA,

            sigma=SIGMA,

            phi=PHI,

            kappa=KAPPA,

            lambda_index=LAMBDA

        )

