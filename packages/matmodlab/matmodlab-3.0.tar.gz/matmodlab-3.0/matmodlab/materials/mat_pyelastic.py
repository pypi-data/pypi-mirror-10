import logging
import numpy as np
from matmodlab.mmd.material import MaterialModel
from matmodlab.femlib.constants import VOIGHT

class PyElastic(MaterialModel):
    name = "pyelastic"

    def __init__(self):
        self.param_names = ["K", "G"]
        self.prop_names = ["K", "G"]

    def mimicking(self, mat_mimic):
        # reset the initial parameter array to represent this material
        iparray = np.zeros(2)
        iparray[0] = mat_mimic.completions["K"] or 0.
        iparray[1] = mat_mimic.completions["G"] or 0.
        if mat_mimic.completions["YT"]:
            logging.getLogger('mps').warn('{0} cannot mimic a strength limit, '
                     'only an elastic response will occur'.format(self.name))
        return iparray

    def setup(self):
        """Set up the Elastic material

        """
        logger = logging.getLogger('mps')
        # Check inputs
        K, G, = self.params
        errors = 0
        if K <= 0.0:
            errors += 1
            logger.error("Bulk modulus K must be positive")
        if G <= 0.0:
            errors += 1
            logger.error("Shear modulus G must be positive")
        nu = (3.0 * K - 2.0 * G) / (6.0 * K + 2.0 * G)
        if nu > 0.5:
            errors += 1
            logger.error("Poisson's ratio > .5")
        if nu < -1.0:
            errors += 1
            logger.error("Poisson's ratio < -1.")
        if nu < 0.0:
            logger.warn("#---- WARNING: negative Poisson's ratio")
        if errors:
            raise ValueError("stopping due to previous errors")

    def update_state(self, time, dtime, temp, dtemp, energy, rho, F0, F,
        stran, d, elec_field, stress, xtra, **kwargs):
        """Compute updated stress given strain increment

        Parameters
        ----------
        dtime : float
            Time step

        d : array_like
            Deformation rate

        stress : array_like
            Stress at beginning of step

        xtra : array_like
            Extra variables

        Returns
        -------
        S : array_like
            Updated stress

        xtra : array_like
            Updated extra variables

        """
        # strains are sent in using engineering shear strains, convert to tensor
        de = d * dtime / VOIGHT
        iso = de[:3].sum() / 3.0 * np.array([1.0, 1.0, 1.0, 0.0, 0.0, 0.0])
        dev = de - iso
        K = self.params["K"]
        G = self.params["G"]
        stress = stress + 3.0 * K * iso + 2.0 * G * dev
        return stress, xtra, self.constant_jacobian
