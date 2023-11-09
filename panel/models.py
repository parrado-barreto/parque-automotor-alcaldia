from django.db import models
#docker-compose up --build

# Create your models here.

class Dependencias(models.Model):
    id_dep = models.AutoField(primary_key=True)
    nom_dep = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'dependencias'


class Usuarios(models.Model):
    id_per = models.BigIntegerField(primary_key=True)
    pas_per = models.CharField(max_length=30, null=False)
    nom_per = models.CharField(max_length=30, null=False)
    ape_per = models.CharField(max_length=30, null=False)
    tel_per = models.CharField(max_length=30, null=False)
    dir_per = models.CharField(max_length=30, null=False)
    cat_per = models.CharField(max_length=30, null=False)
    vig_per = models.DateField(null=True)
    pase_ade_per = models.ImageField(upload_to="imagenes", null=True)
    pase_atr_per = models.ImageField(upload_to="imagenes", null=True)
    dep_per = models.ForeignKey(Dependencias, on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuarios'


class Soat(models.Model):
    id_soa = models.AutoField(primary_key=True)
    nom_emp_soa = models.CharField(max_length=50, null=True)
    fec_exp_soa = models.DateField(null=True)
    fec_vig_soa = models.DateField(null=True)
    fec_ven_soa = models.DateField(null=True)

    class Meta:
        db_table = 'soat'


class Tecnicomecanica(models.Model):
    id_tec = models.AutoField(primary_key=True)
    nom_emp_tec = models.CharField(max_length=50, null=True)
    fec_exp_tec = models.DateField(null=True)
    fec_ven_tec = models.DateField(null=True)

    class Meta:
        db_table = 'tecnicomecanica'


class Vehiculos(models.Model):
    pla_veh = models.CharField(max_length=10, primary_key=True)
    num_lic_veh = models.BigIntegerField(null=False)
    cla_veh = models.CharField(max_length=50, null=False)
    mar_veh = models.CharField(max_length=50, null=False)
    mod_veh = models.IntegerField(null=False)
    col_veh = models.CharField(max_length=30, null=False)
    num_mot_veh = models.CharField(max_length=50, null=False)
    num_cha_veh = models.CharField(max_length=50, null=False)
    cil_veh = models.IntegerField(null=False)
    tip_car_veh = models.CharField(max_length=50, null=False)
    est_veh = models.BooleanField(null=False)
    obs_veh = models.CharField(max_length=200, null=True)
    dep_veh = models.ForeignKey(Dependencias,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    per_asi_veh = models.ManyToManyField(Usuarios,
                                         through='VehiculosAsignados',
                                         blank=True)
    soa_veh = models.ForeignKey(Soat,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)
    tec_veh = models.ForeignKey(Tecnicomecanica,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)

    class Meta:
        db_table = 'vehiculos'


class VehiculosAsignados(models.Model):
    id_per = models.ForeignKey(Usuarios,
                               blank=True,
                               on_delete=models.CASCADE)
    id_veh = models.ForeignKey(Vehiculos,
                               blank=True,
                               on_delete=models.CASCADE)
    fec_ing = models.DateTimeField(auto_now_add=True, null=True)
    fec_sal = models.DateTimeField(null=True)
    obs_veh_asi = models.CharField(max_length=200)

    class Meta:
        db_table = 'vehiculos_asignados'


class Preoperacionalesm(models.Model):
    id_pre = models.AutoField(primary_key=True)
    niv_pre = models.CharField(max_length=20, null=False)
    man_pre = models.CharField(max_length=20, null=False)
    dir_pre = models.CharField(max_length=20, null=False)
    gua_pre = models.CharField(max_length=20, null=False)
    cha_pre = models.CharField(max_length=20, null=False)
    sus_pre = models.CharField(max_length=20, null=False)
    fre_pre = models.CharField(max_length=20, null=False)
    lla_pre = models.CharField(max_length=20, null=False)
    rin_pre = models.CharField(max_length=20, null=False)
    tre_pre = models.CharField(max_length=20, null=False)
    exo_pre = models.CharField(max_length=20, null=False)
    ret_pre = models.CharField(max_length=20, null=False)
    man_mec_pre = models.CharField(max_length=20, null=False)
    luc_pre = models.CharField(max_length=20, null=False)
    dir_stop_pre = models.CharField(max_length=20, null=False)
    pit_pre = models.CharField(max_length=20, null=False)
    obs_pre = models.CharField(max_length=500)
    fec_pre = models.DateField(null=True)
    pla_pre = models.ForeignKey(Vehiculos,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

    class Meta:
        db_table = 'preoperacionalesm'


class Preoperacionalesc(models.Model):
    id_pre = models.AutoField(primary_key=True)
    dir_del_pre = models.CharField(max_length=20, null=False)
    dir_tra_pre = models.CharField(max_length=20, null=False)
    sis_luc_pre = models.CharField(max_length=20, null=False)
    luc_fre_pre = models.CharField(max_length=20, null=False)
    luc_rev_pre = models.CharField(max_length=20, null=False)
    luc_par_pre = models.CharField(max_length=20, null=False)
    vpan_pre = models.CharField(max_length=20, null=False)
    vlat_pre = models.CharField(max_length=20, null=False)
    vtra_pre = models.CharField(max_length=20, null=False)
    limp_pre = models.CharField(max_length=20, null=False)
    elat_pre = models.CharField(max_length=20, null=False)
    eret_pre = models.CharField(max_length=20, null=False)
    pit_pre = models.CharField(max_length=20, null=False)
    taco_pre = models.CharField(max_length=20, null=False)
    odo_pre = models.CharField(max_length=20, null=False)
    gas_pre = models.CharField(max_length=20, null=False)
    tem_pre = models.CharField(max_length=20, null=False)
    cin_pre = models.CharField(max_length=20, null=False)
    alar_pre = models.CharField(max_length=20, null=False)
    cha_pue_pre = models.CharField(max_length=20, null=False)
    pue_cie_pre = models.CharField(max_length=20, null=False)
    esc_acc_pre = models.CharField(max_length=20, null=False)
    pas_tec_pre = models.CharField(max_length=20, null=False)
    ven_eme_pre = models.CharField(max_length=20, null=False)
    alc_vol_pre = models.CharField(max_length=20, null=False)
    fre_pri_pre = models.CharField(max_length=20, null=False)
    fre_man_pre = models.CharField(max_length=20, null=False)
    agu_lim_pre = models.CharField(max_length=20, null=False)
    agu_ref_pre = models.CharField(max_length=20, null=False)
    ace_mot_pre = models.CharField(max_length=20, null=False)
    liq_fre_pre = models.CharField(max_length=20, null=False)
    liq_bat_pre = models.CharField(max_length=20, null=False)
    ace_hid_pre = models.CharField(max_length=20, null=False)
    cor_pre = models.CharField(max_length=20, null=False)
    man_pre = models.CharField(max_length=20, null=False)
    est_lla_pre = models.CharField(max_length=20, null=False)
    pre_lla_pre = models.CharField(max_length=20, null=False)
    lab_lla_pre = models.CharField(max_length=20, null=False)
    rep_lla_pre = models.CharField(max_length=20, null=False)
    señ_eme_pre = models.CharField(max_length=20, null=False)
    tac_pre = models.CharField(max_length=20, null=False)
    cha_pre = models.CharField(max_length=20, null=False)
    gat_pre = models.CharField(max_length=20, null=False)
    gua_pre = models.CharField(max_length=20, null=False)
    cru_pre = models.CharField(max_length=20, null=False)
    her_pre = models.CharField(max_length=20, null=False)
    bot_pre = models.CharField(max_length=20, null=False)
    ext_pre = models.CharField(max_length=20, null=False)
    obs_pre = models.CharField(max_length=500)
    fec_pre = models.DateField(null=True)
    pla_pre = models.ForeignKey(Vehiculos,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

    class Meta:
        db_table = 'preoperacionalesc'


class Mantenimiento(models.Model):
    id_man = models.AutoField(primary_key=True)
    fec_man = models.DateField(null=True)
    tipo_man = models.CharField(max_length=20, null=False)
    des_obs_man = models.CharField(max_length=500)
    per_man = models.CharField(max_length=50, null=False)
    rec_man = models.CharField(max_length=200)
    id_veh = models.ForeignKey(Vehiculos,
                               blank=True,
                               on_delete=models.CASCADE)

    class Meta:
        db_table = 'mantenimiento'
