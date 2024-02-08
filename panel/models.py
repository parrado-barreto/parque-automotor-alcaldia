from django.db import models
#docker-compose up --build

# Create your models here.

class Dependencias(models.Model):
    id_dep = models.AutoField(primary_key=True)
    nom_dep = models.CharField(max_length=100, null=False)

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
    pase_ade_per = models.FileField(upload_to="imagenes", null=True, blank=True)
    pase_atr_per = models.FileField(upload_to="imagenes", null=True, blank=True)
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

class Periodicasm(models.Model):
    id_periodica = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    kilometraje = models.IntegerField(null=False)
    pla_per = models.ForeignKey(Vehiculos,
                               blank=True,
                               on_delete=models.CASCADE)
    encendido = models.CharField(max_length=20, null=False)
    defensa = models.CharField(max_length=20, null=False)
    llaves = models.CharField(max_length=20, null=False)
    carburador = models.CharField(max_length=20, null=False)
    autocarburador = models.CharField(max_length=20, null=False)
    bobina_encendido = models.CharField(max_length=20, null=False)
    bobina_alta = models.CharField(max_length=20, null=False)
    bateria = models.CharField(max_length=20, null=False)
    bujia = models.CharField(max_length=20, null=False)
    capuchon_bujia = models.CharField(max_length=20, null=False)
    punzon = models.CharField(max_length=20, null=False)
    pata = models.CharField(max_length=20, null=False)
    kit_arrastre = models.CharField(max_length=20, null=False)
    tapa_pinon = models.CharField(max_length=20, null=False)
    guia_cadena = models.CharField(max_length=20, null=False)
    guarda_cadena = models.CharField(max_length=20, null=False)
    patada_crank = models.CharField(max_length=20, null=False)
    tacometro = models.CharField(max_length=20, null=False)
    perilla_tacometro = models.CharField(max_length=20, null=False)
    switch = models.CharField(max_length=20, null=False)
    palanca_cambios = models.CharField(max_length=20, null=False)
    guayas = models.CharField(max_length=20, null=False)
    guardabarros = models.CharField(max_length=20, null=False)
    rines = models.CharField(max_length=20, null=False)
    inyeccion = models.CharField(max_length=20, null=False)
    guias_aire = models.CharField(max_length=20, null=False)
    sirena = models.CharField(max_length=20, null=False)
    llanta_delantera = models.CharField(max_length=20, null=False)
    llanta_trasera = models.CharField(max_length=20, null=False)
    manillares = models.CharField(max_length=20, null=False)
    protector_manillar = models.CharField(max_length=20, null=False)
    mango_acelerador = models.CharField(max_length=20, null=False)
    manubrio = models.CharField(max_length=20, null=False)
    mando_luces = models.CharField(max_length=20, null=False)
    maniguetas = models.CharField(max_length=20, null=False)
    herramientas = models.CharField(max_length=20, null=False)
    pastillas_delanteras = models.CharField(max_length=20, null=False)
    pastillas_traseras = models.CharField(max_length=20, null=False)
    bandas = models.CharField(max_length=20, null=False)
    tapas_laterales = models.CharField(max_length=20, null=False)
    carenaje = models.CharField(max_length=20, null=False)
    tanque = models.CharField(max_length=20, null=False)
    tapa_tanque = models.CharField(max_length=20, null=False)
    exhosto = models.CharField(max_length=20, null=False)
    rejillas_exhosto = models.CharField(max_length=20, null=False)
    telescopios = models.CharField(max_length=20, null=False)
    tapa_telescopios = models.CharField(max_length=20, null=False)
    cauchos_telescopios = models.CharField(max_length=20, null=False)
    direccionales = models.CharField(max_length=20, null=False)
    control_luces = models.CharField(max_length=20, null=False)
    strober_delantero = models.CharField(max_length=20, null=False)
    strober_trasero = models.CharField(max_length=20, null=False)
    descargapies = models.CharField(max_length=20, null=False)
    tanque_aceite = models.CharField(max_length=20, null=False)
    tapa_tanque_aceite = models.CharField(max_length=20, null=False)
    pastas_reflectoras = models.CharField(max_length=20, null=False)
    sillin = models.CharField(max_length=20, null=False)
    porta_placa = models.CharField(max_length=20, null=False)
    tijera = models.CharField(max_length=20, null=False)
    espejos = models.CharField(max_length=20, null=False)
    farola = models.CharField(max_length=20, null=False)
    rectificador_corriente = models.CharField(max_length=20, null=False)
    flancher = models.CharField(max_length=20, null=False)
    cdi = models.CharField(max_length=20, null=False)
    stop = models.CharField(max_length=20, null=False)
    monoshock = models.CharField(max_length=20, null=False)
    velocimetro = models.CharField(max_length=20, null=False)
    casco = models.CharField(max_length=20, null=False)
    chaleco = models.CharField(max_length=20, null=False)
    estado_higiene = models.BooleanField(null=False)
    foto_1 = models.FileField(upload_to="imagenes", null=True, blank=True)
    foto_2 = models.FileField(upload_to="imagenes", null=True, blank=True)
    foto_3 = models.FileField(upload_to="imagenes", null=True, blank=True)
    foto_4 = models.FileField(upload_to="imagenes", null=True, blank=True)
    observaciones = models.CharField(max_length=500, null=True)
    class Meta:
        db_table = 'periodicasm'
