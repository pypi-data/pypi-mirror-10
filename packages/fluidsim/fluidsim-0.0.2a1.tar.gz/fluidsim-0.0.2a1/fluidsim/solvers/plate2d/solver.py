# -*- coding: utf-8 -*-

"""Plate2d solver (:mod:`fluidsim.solvers.plate2d.solver`)
================================================================

.. currentmodule:: fluidsim.solvers.plate2d.solver

Provides:

.. autoclass:: Simul
   :members:
   :private-members:

.. todo::

   - bench performances,
   - output:
     * spectra,
     * spatial means (energy, dissipation, forcing),
     * correlations frequencies,
   - forcing,
   - solver solving exactly the linear terms.

"""

from __future__ import print_function

import numpy as np

from fluidsim.base.setofvariables import SetOfVariables
from fluidsim.base.solvers.pseudo_spect import (
    SimulBasePseudoSpectral, InfoSolverPseudoSpectral)


class InfoSolverPlate2D(InfoSolverPseudoSpectral):
    def _init_root(self):

        super(InfoSolverPlate2D, self)._init_root()

        package = 'fluidsim.solvers.plate2d'
        self.module_name = package + '.solver'
        self.class_name = 'Simul'
        self.short_name = 'Plate2D'

        classes = self.classes

        classes.State.module_name = package + '.state'
        classes.State.class_name = 'StatePlate2D'

        classes.InitFields.module_name = package + '.init_fields'
        classes.InitFields.class_name = 'InitFieldsPlate2D'

        classes.Output.module_name = package + '.output'
        classes.Output.class_name = 'Output'

        classes.Forcing.module_name = package + '.forcing'
        classes.Forcing.class_name = 'ForcingPlate2D'


class Simul(SimulBasePseudoSpectral):
    r"""Pseudo-spectral solver solving the Föppl-von Kármán equations.

    Notes
    -----

    .. |p| mathmacro:: \partial

    This class is dedicated to solve with a pseudo-spectral method the
    Föppl-von Kármán equations which describe the dynamics of a rigid
    plate.  Using the non-dimensional variables displacement :math:`z`
    and out of plane velocity :math:`w`:

    .. math::
       \p_t z = w,

    .. math::
       \p_t w = - \Delta^2 z + N_w(z) + f_w - \nu_\alpha (-\Delta)^\alpha w.

    where :math:`\Delta = \p_{xx} + \p_{yy}` is the Laplacian. The
    first term of the two equations corresponds to the linear part.
    :math:`f_w` and :math:`\nu_\alpha \Delta^\alpha w` are the
    forcing and the dissipation terms, respectively. The nonlinear
    term is equal to :math:`N_w(z) = \{ z, \chi \}`, where :math:`\{
    \cdot, \cdot \}` is the Monge-Ampère operator

    .. math::
       \{ a, b \} = \p_{xx} a \p_{yy} b + \p_{yy} a \p_{xx} b
       - 2 \p_{xy} a \p_{xy} b,

    and

    .. math:: \Delta^2 \chi = -\{ z, z \}.

    Taking the Fourier transform, we get:

    .. math::
       \p_t \hat z = \hat w,

    .. math::
       \p_t \hat w = - k^4 \hat z + \widehat{N_w(z)} + \hat f_w
       - \nu_\alpha k^{2\alpha} \hat w,

    where :math:`k^2 = |\mathbf{k}|^2`. For this simple solver, we
    will use the variables :math:`z` and :math:`w` and only the
    dissipative term will be solve exactly.  Thus, all the other terms
    are included in the :func:`tendencies_nonlin` function.

    **Energetics**: The total energy can be decomposed in the kinetic energy

    .. math::
       E_K = \frac{1}{2} \langle w^2 \rangle
       = \frac{1}{2} \sum_\mathbf{k} |\hat w|^2,

    the flexion energy

    .. math::
       E_L = \frac{1}{2} \langle (\Delta z)^2 \rangle
       = \frac{1}{2} \sum_\mathbf{k} k^4|\hat z|^2,

    and the non-quadratic extension energy

    .. math::
       E_E = \frac{1}{4} \langle (\Delta \chi)^2 \rangle
       = \frac{1}{4} \sum_\mathbf{k} k^4 |\hat \chi|^2.

    The energy injected into the system by the forcing is

    .. math::
       P = \langle f_w w \rangle,

    and the dissipation is

    .. math::
       D = \nu_\alpha \langle w (-\Delta)^\alpha w \rangle.

    """

    InfoSolver = InfoSolverPlate2D

    @staticmethod
    def _complete_params_with_default(params):
        """This static method is used to complete the *params* container.
        """
        SimulBasePseudoSpectral._complete_params_with_default(params)
        attribs = {'beta': 0.}
        params._set_attribs(attribs)

    def tendencies_nonlin(self, state_fft=None):
        """Compute the "nonlinear" tendencies."""
        oper = self.oper

        if state_fft is None:
            state_fft = self.state.state_fft

        w_fft = state_fft.get_var('w_fft')
        z_fft = state_fft.get_var('z_fft')

        mamp_zz = oper.monge_ampere_from_fft(z_fft, z_fft)
        chi_fft = - oper.invlaplacian2_fft(oper.fft2(mamp_zz))
        mamp_zchi = oper.monge_ampere_from_fft(z_fft, chi_fft)
        Nw_fft = oper.fft2(mamp_zchi)
        lap2z_fft = oper.laplacian2_fft(z_fft)
        F_fft = - lap2z_fft + Nw_fft

        oper.dealiasing(F_fft)
        oper.dealiasing(w_fft)

        tendencies_fft = SetOfVariables(
            like=self.state.state_fft,
            info='tendencies_nonlin')

        tendencies_fft.set_var('w_fft', F_fft)
        tendencies_fft.set_var('z_fft', w_fft)

        # ratio = self.test_tendencies_nonlin(
        #     tendencies_fft, w_fft, z_fft, chi_fft)
        # print('ratio:', ratio)

        if self.params.FORCING:
            tendencies_fft += self.forcing.get_forcing()

        return tendencies_fft

    def compute_freq_diss(self):
        """Compute the dissipation frequencies with dissipation only for w."""
        f_d_w, f_d_hypo_w = super(Simul, self).compute_freq_diss()
        f_d = np.zeros_like(self.state.state_fft, dtype=np.float64)
        f_d_hypo = np.zeros_like(self.state.state_fft,
                                 dtype=np.float64)
        f_d[0] = f_d_w
        f_d_hypo[0] = f_d_hypo_w
        return f_d, f_d_hypo

    def test_tendencies_nonlin(
            self, tendencies_fft=None,
            w_fft=None, z_fft=None, chi_fft=None):
        r"""Test if the tendencies conserves the total energy.

        We consider the conservative Föppl-von Kármán equations
        (without dissipation and forcing) written as

        .. math::

           \p_t z = F_z

           \p_t w = F_w

        We have:

        .. math::

           \p_t E_K(\mathbf{k}) = \mathcal{R} ( \hat F_w \hat w ^* )

           \p_t E_L(\mathbf{k}) = k^4 \mathcal{R} ( \hat F_z \hat z ^* )

           \p_t E_{NQ}(\mathbf{k}) =
           - \mathcal{R} ( \widehat{\{ F_z, z\}} \hat \chi ^* )

        Since the total energy is conserved, we should have

        .. math::

           \sum_{\mathbf{k}} \p_t E_K(\mathbf{k}) + \p_t E_L(\mathbf{k})
           + \p_t E_{NQ}(\mathbf{k}) = 0

        This function computes this quantities.

        """

        if tendencies_fft is None:
            tendencies_fft = self.tendencies_nonlin()
            w_fft = self.state.state_fft.get_var('w_fft')
            z_fft = self.state.state_fft.get_var('z_fft')
            chi_fft = self.state.compute('chi_fft')

        F_w_fft = tendencies_fft.get_var('w_fft')
        F_z_fft = tendencies_fft.get_var('z_fft')

        K4 = self.oper.K4

        dt_E_K = np.real(F_w_fft * w_fft.conj())
        dt_E_L = K4 * np.real(F_z_fft * z_fft.conj())

        tmp = self.oper.monge_ampere_from_fft(F_z_fft, z_fft)
        tmp_fft = self.oper.fft2(tmp)

        dt_E_NQ = - np.real(tmp_fft * chi_fft.conj())

        T = dt_E_K + dt_E_L + dt_E_NQ

        norm = self.oper.sum_wavenumbers(abs(T))

        if norm < 1e-15:
            print('Only zeros in total energy tendency.')
            # print('(K+L)\n', dt_E_K+dt_E_L)
            # print('NQ\n', dt_E_NQ)
            return 0
        else:
            T = T/norm
            # print('ratio array\n', T)
            # print('(K+L)\n', (dt_E_K+dt_E_L)/norm)
            # print('NQ\n', dt_E_NQ/norm)
            return self.oper.sum_wavenumbers(T)


if __name__ == "__main__":

    np.set_printoptions(precision=2)

    import fluiddyn as fld

    params = Simul.create_default_params()

    params.short_name_type_run = 'test'

    nh = 192/2
    Lh = 1.
    params.oper.nx = nh
    params.oper.ny = nh
    params.oper.Lx = Lh
    params.oper.Ly = Lh
    # params.oper.type_fft = 'FFTWPY'
    params.oper.coef_dealiasing = 2./3

    delta_x = Lh/nh
    params.nu_8 = 2.*10e-4*params.forcing.forcing_rate**(1./3)*delta_x**8

    kmax = np.sqrt(2)*np.pi/delta_x

    params.time_stepping.USE_CFL = False
    params.time_stepping.deltat0 = 2*np.pi/kmax**2/4
    params.time_stepping.USE_T_END = True
    params.time_stepping.t_end = 1.
    params.time_stepping.it_end = 1

    # params.init_fields.type = 'HARMONIC'
    params.init_fields.type = 'noise'
    params.init_fields.noise.velo_max = 0.001
    # params.init_fields.path_file = (
    #     '/home/users/bonamy2c/Sim_data/PLATE2D_test_L='
    #     '2pix2pi_256x256_2015-03-04_22-36-37/state_phys_t=000.100.hd5')

    params.FORCING = True
    params.forcing.type = 'random'
    params.forcing.forcing_rate = 1.
    # params.forcing.nkmax_forcing = 5
    # params.forcing.nkmin_forcing = 4

    params.output.periods_print.print_stdout = 0.05

    params.output.periods_save.phys_fields = 5.
    params.output.periods_save.spectra = 1.
    params.output.periods_save.spatial_means = 0.0005
    # params.output.periods_save.spect_energy_budg = 0.5
    # params.output.periods_save.increments = 0.5
    # params.output.periods_save.correl_freq = 0.9*params.time_stepping.deltat0

    params.output.ONLINE_PLOT_OK = True
    params.output.period_refresh_plots = 0.1
    params.output.periods_plot.phys_fields = 0.

    params.output.phys_fields.field_to_plot = 'z'

    params.output.spectra.HAS_TO_PLOT_SAVED = False
    params.output.spatial_means.HAS_TO_PLOT_SAVED = True

    params.output.correl_freq.HAS_TO_PLOT_SAVED = False

    sim = Simul(params)

    # sim.output.phys_fields.plot()
    sim.time_stepping.start()
#    sim.output.phys_fields.plot()

    fld.show()
