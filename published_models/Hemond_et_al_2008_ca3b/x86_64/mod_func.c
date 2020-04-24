#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _KahpM95_reg(void);
extern void _cacumm_reg(void);
extern void _cagk_reg(void);
extern void _cal2_reg(void);
extern void _can2_reg(void);
extern void _cat_reg(void);
extern void _distr_reg(void);
extern void _h_reg(void);
extern void _kaprox_reg(void);
extern void _kd_reg(void);
extern void _kdrca1_reg(void);
extern void _km_reg(void);
extern void _na3n_reg(void);
extern void _naxn_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," KahpM95.mod");
    fprintf(stderr," cacumm.mod");
    fprintf(stderr," cagk.mod");
    fprintf(stderr," cal2.mod");
    fprintf(stderr," can2.mod");
    fprintf(stderr," cat.mod");
    fprintf(stderr," distr.mod");
    fprintf(stderr," h.mod");
    fprintf(stderr," kaprox.mod");
    fprintf(stderr," kd.mod");
    fprintf(stderr," kdrca1.mod");
    fprintf(stderr," km.mod");
    fprintf(stderr," na3n.mod");
    fprintf(stderr," naxn.mod");
    fprintf(stderr, "\n");
  }
  _KahpM95_reg();
  _cacumm_reg();
  _cagk_reg();
  _cal2_reg();
  _can2_reg();
  _cat_reg();
  _distr_reg();
  _h_reg();
  _kaprox_reg();
  _kd_reg();
  _kdrca1_reg();
  _km_reg();
  _na3n_reg();
  _naxn_reg();
}
