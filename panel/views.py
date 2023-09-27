from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios, Dependencias, Vehiculos, Soat, Tecnicomecanica, VehiculosAsignados, Preoperacionalesm, Preoperacionalesc, Mantenimiento
from django.db.models import Q
from datetime import date
from django.contrib import messages

# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request,"index.html")

def listar(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Usuarios.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_per__icontains=busqueda) |
            Q(nom_per__icontains=busqueda) |
            Q(ape_per__icontains=busqueda) |
            Q(tel_per__icontains=busqueda) |
            Q(dir_per__icontains=busqueda) |
            Q(cat_per__icontains=busqueda) |
            Q(vig_per__icontains=busqueda) |
            Q(dep_per__icontains=busqueda) 
            )
            datos = {'usuarios': res_busqueda}
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            return render(request, "crud_usuarios/listar.html", datos)
        else:
            datos = { 'usuarios' : lista }
            return render(request, "crud_usuarios/listar.html", datos)
    else:
        users = Usuarios.objects.order_by('-id_per')[:10]
        datos = { 'usuarios' : users }
        return render(request, "crud_usuarios/listar.html", datos)
   
def agregar(request):
    if request.method == 'POST':
        if request.POST.get('pas_per') and request.POST.get('nom_per') and request.POST.get('ape_per') and request.POST.get('tel_per') and request.POST.get('dir_per') and request.POST.get('cat_per') and request.POST.get('vig_per') and request.POST.get('dep_per'):
            try:
                user = Usuarios()
                user.id_per = request.POST.get('id_per')
                user.pas_per = request.POST.get('pas_per')
                user.nom_per = request.POST.get('nom_per')
                user.ape_per = request.POST.get('ape_per')
                user.tel_per = request.POST.get('tel_per')
                user.dir_per = request.POST.get('dir_per')
                user.cat_per = request.POST.get('cat_per')
                user.vig_per = request.POST.get('vig_per')
                user.pase_ade_per = request.POST.get('pase_ade_per')
                user.dep_per_id = request.POST.get('dep_per')
                user.save()
                messages.success(request, 'El usuario {} fue agregado'.format(user.nom_per+" "+user.ape_per))
                return redirect('listar')
            except:
                messages.error(request, 'Ha ocurrido un error en los datos, intentalo nuevamente por favor')
                return redirect('agregar')
    else:
        users = Usuarios.objects.all()
        deps = Dependencias.objects.all()
        datos = {'usuarios' : users, 'dependencias': deps}
        return render(request,"crud_usuarios/agregar.html",datos)

def actualizar(request, idUsuario):
    try:
        if request.method == 'POST':
            if request.POST.get('pas_per') and request.POST.get('nom_per') and request.POST.get('ape_per') and request.POST.get('tel_per') and request.POST.get('dir_per') and request.POST.get('cat_per') and request.POST.get('vig_per') and request.POST.get('dep_per'):
                user = Usuarios()
                user.id_per = request.POST.get('id')
                user.pas_per = request.POST.get('pas_per')
                user.nom_per = request.POST.get('nom_per')
                user.ape_per = request.POST.get('ape_per')
                user.tel_per = request.POST.get('tel_per')
                user.dir_per = request.POST.get('dir_per')
                user.cat_per = request.POST.get('cat_per')
                user.vig_per = request.POST.get('vig_per')
                user.dep_per_id = request.POST.get('dep_per')
                user.save()
                messages.success(request, 'El usuario {} fue modificado'.format(user.nom_per+" "+user.ape_per))
                return redirect('listar')
        else:
            users = Usuarios.objects.all()
            user = Usuarios.objects.get( id_per=idUsuario )
            user.vig_per = date.strftime(user.vig_per, "%Y-%m-%d")
            deps = Dependencias.objects.all()
            datos = { 'usuarios' : users , 'usuario' : user , 'dependencias': deps}
            return render(request, "crud_usuarios/actualizar.html", datos)
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        deps = Dependencias.objects.all()
        datos = { 'usuarios' : users , 'usuario' : user , 'dependencias': deps}
        return render(request, "crud_usuarios/actualizar.html", datos)

def eliminar(request, idUsuario):
    try:
        if request.method=='POST':
            if request.POST.get('id_per'):
                id_a_borrar= request.POST.get('id_per')
                tupla=Usuarios.objects.get(id_per = id_a_borrar)
                tupla.delete()
                messages.warning(request, 'El usuario {} fue eliminado'.format(tupla.nom_per+" "+tupla.ape_per))
                return redirect('listar')
        else:
            users = Usuarios.objects.all()
            user = Usuarios.objects.get(id_per=idUsuario)
            datos = { 'usuarios' : users , 'usuario' : user}
            return render(request, "crud_usuarios/eliminar.html", datos)
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos = { 'usuarios' : users , 'usuario' : user}
        return render(request, "crud_usuarios/eliminar.html", datos)

def listardep(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Dependencias.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_dep__icontains=busqueda) |
            Q(nom_dep__icontains=busqueda) 
            )
            datos = {'dependencias': res_busqueda}
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            return render(request, "crud_dependencias/listar.html", datos)
        else:
            datos = { 'dependencias' : lista }
            return render(request, "crud_dependencias/listar.html", datos)
    else:
        deps = Dependencias.objects.order_by('-id_dep')[:10]
        datos = { 'dependencias' : deps }
        return render(request, "crud_dependencias/listar.html", datos)

def agregardep(request):
    if request.method == 'POST':
        if request.POST.get('nom_dep'):
            
            dep = Dependencias()
            dep.nom_dep = request.POST.get('nom_dep')
            dep.save()
            messages.success(request, 'La dependencia {} fue agregada'.format(dep.nom_dep))
            return redirect('listardep')
    else:
        deps = Dependencias.objects.all()
        datos = {'dependencias' : deps}
        return render(request,"crud_dependencias/agregar.html",datos)

def actualizardep(request, idDependencia):
    try:
        if request.method == 'POST':
            if request.POST.get('nom_dep'):
                dep = Dependencias()
                dep.id_dep = request.POST.get('id')
                dep.nom_dep = request.POST.get('nom_dep')
                dep.save()
                messages.success(request, 'La dependencia {} fue modificada'.format(dep.nom_dep))
                return redirect('listardep')
        else:
            deps = Dependencias.objects.all()
            dep = Dependencias.objects.get( id_dep=idDependencia )
            datos = { 'dependencias' : deps , 'dependencia' : dep }
            return render(request, "crud_dependencias/actualizar.html", datos)
    except Dependencias.DoesNotExist:
        deps = Dependencias.objects.all()
        dep = None
        datos = { 'dependencias' : deps , 'dependencia' : dep }
        return render(request, "crud_dependencias/actualizar.html", datos)

def eliminardep(request, idDependencia):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar= request.POST.get('id')
                tupla=Dependencias.objects.get(id_dep = id_a_borrar)
                tupla.delete()
                messages.success(request, 'La dependencia {} fue eliminada'.format(tupla.nom_dep))
                return redirect('listardep')
        else:
            deps = Dependencias.objects.all()
            dep = Dependencias.objects.get( id_dep=idDependencia )
            datos = { 'dependencias' : deps , 'dependencia' : dep }
            return render(request, "crud_dependencias/eliminar.html", datos)
    except Dependencias.DoesNotExist:
        deps = Dependencias.objects.all()
        dep = None
        datos = { 'dependencias' : deps , 'dependencia' : dep }
        return render(request, "crud_dependencias/eliminar.html", datos)    
    
def listarveh(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Vehiculos.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(pla_veh__icontains=busqueda) |
            Q(num_lic_veh__icontains=busqueda) |
            Q(cla_veh__icontains=busqueda) |
            Q(mar_veh__icontains=busqueda) |
            Q(mod_veh__icontains=busqueda) |
            Q(col_veh__icontains=busqueda) |
            Q(num_mot_veh__icontains=busqueda) |
            Q(num_cha_veh__icontains=busqueda) |
            Q(cil_veh__icontains=busqueda) |
            Q(tip_car_veh__icontains=busqueda) |
            Q(est_veh__icontains=busqueda) |
            Q(obs_veh__icontains=busqueda) 
            )
            datos = {'vehiculos': res_busqueda}
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            return render(request, "crud_vehiculos/listar.html", datos)
        else:
            datos = { 'vehiculos' : lista }
            return render(request, "crud_vehiculos/listar.html", datos)
    else:
        vehs = Vehiculos.objects.order_by('-pla_veh')[:10]
        datos = { 'vehiculos' : vehs }
        return render(request, "crud_vehiculos/listar.html", datos)
    
def agregarveh(request):
    if request.method == 'POST':
        if  request.POST.get('pla_veh') and request.POST.get('num_lic_veh') and request.POST.get('cla_veh') and request.POST.get('mar_veh') and request.POST.get('mod_veh') and request.POST.get('col_veh') and request.POST.get('num_mot_veh') and request.POST.get('num_cha_veh') and request.POST.get('cil_veh') and request.POST.get('tip_car_veh') and request.POST.get('est_veh') and request.POST.get('dep_veh') and request.POST.get('soa_veh') and request.POST.get('tec_veh'):
            veh = Vehiculos()
            veh.pla_veh = request.POST.get('pla_veh')
            veh.num_lic_veh = request.POST.get('num_lic_veh')
            veh.cla_veh = request.POST.get('cla_veh')
            veh.mar_veh = request.POST.get('mar_veh')
            veh.mod_veh = request.POST.get('mod_veh')
            veh.col_veh = request.POST.get('col_veh')
            veh.num_mot_veh = request.POST.get('num_mot_veh')
            veh.num_cha_veh = request.POST.get('num_cha_veh')
            veh.cil_veh = request.POST.get('cil_veh')
            veh.tip_car_veh = request.POST.get('tip_car_veh')
            veh.est_veh = request.POST.get('est_veh')
            veh.obs_veh = request.POST.get('obs_veh')
            veh.dep_veh_id = request.POST.get('dep_veh')
            veh.soa_veh_id = request.POST.get('soa_veh')
            veh.tec_veh_id = request.POST.get('tec_veh')
            veh.save()
            messages.success(request, 'El vehiculo de placas {} fue agregado'.format(veh.pla_veh))
            return redirect('listarveh')
    else:
        vehs = Vehiculos.objects.all()
        deps = Dependencias.objects.all()
        soats = Soat.objects.all()
        tecs = Tecnicomecanica.objects.all()
        datos = {'vehiculos' : vehs, 'dependencias' : deps,'soats': soats, 'tecs': tecs}
        return render(request,"crud_vehiculos/agregar.html",datos)

def actualizarveh(request, idVehiculo):
    try:
        if request.method == 'POST':
           if  request.POST.get('id') and request.POST.get('num_lic_veh') and request.POST.get('cla_veh') and request.POST.get('mar_veh') and request.POST.get('mod_veh') and request.POST.get('col_veh') and request.POST.get('num_mot_veh') and request.POST.get('num_cha_veh') and request.POST.get('cil_veh') and request.POST.get('tip_car_veh') and request.POST.get('est_veh') and request.POST.get('dep_veh') and request.POST.get('soa_veh') and request.POST.get('tec_veh'):
                veh = Vehiculos()
                veh.pla_veh = request.POST.get('id')
                veh.num_lic_veh = request.POST.get('num_lic_veh')
                veh.cla_veh = request.POST.get('cla_veh')
                veh.mar_veh = request.POST.get('mar_veh')
                veh.mod_veh = request.POST.get('mod_veh')
                veh.col_veh = request.POST.get('col_veh')
                veh.num_mot_veh = request.POST.get('num_mot_veh')
                veh.num_cha_veh = request.POST.get('num_cha_veh')
                veh.cil_veh = request.POST.get('cil_veh')
                veh.tip_car_veh = request.POST.get('tip_car_veh')
                veh.est_veh = request.POST.get('est_veh')
                veh.obs_veh = request.POST.get('obs_veh')
                veh.dep_veh_id = request.POST.get('dep_veh')
                veh.soa_veh_id = request.POST.get('soa_veh')
                veh.tec_veh_id = request.POST.get('tec_veh')
                veh.save()
                messages.success(request, 'El vehiculo de placas {} fue modificado'.format(veh.pla_veh))
                return redirect('listarveh')
        else:
            veh = Vehiculos.objects.get( pla_veh=idVehiculo )
            vehs = Vehiculos.objects.all()
            deps = Dependencias.objects.all()
            soats = Soat.objects.all()
            tecs = Tecnicomecanica.objects.all()
            datos = {'vehiculos' : vehs,'vehiculo' : veh, 'dependencias' : deps,'soats': soats, 'tecs': tecs}
            return render(request,"crud_vehiculos/actualizar.html",datos)
    except Vehiculos.DoesNotExist:
        veh = None
        vehs = Vehiculos.objects.all()
        deps = Dependencias.objects.all()
        soats = Soat.objects.all()
        tecs = Tecnicomecanica.objects.all()
        datos = {'vehiculos' : vehs,'vehiculo' : veh, 'dependencias' : deps,'soats': soats, 'tecs': tecs}
        return render(request,"crud_vehiculos/actualizar.html",datos)

def eliminarveh(request, idVehiculo):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar= request.POST.get('id')
                tupla=Vehiculos.objects.get(pla_veh = id_a_borrar)
                tupla.delete()
                messages.success(request, 'El vehiculo de placas {} fue eliminado'.format(tupla.pla_veh))
                return redirect('listarveh')
        else:
            vehs = Vehiculos.objects.all()
            veh = Vehiculos.objects.get( pla_veh=idVehiculo )
            datos = { 'vehiculos' : vehs , 'vehiculo' : veh }
            return render(request, "crud_vehiculos/eliminar.html", datos)
    except Vehiculos.DoesNotExist:
        vehs = Vehiculos.objects.all()
        veh = None
        datos = { 'vehiculos' : vehs , 'vehiculo' : veh }
        return render(request, "crud_vehiculos/eliminar.html", datos)

def listarsoa(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Soat.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_soa__icontains=busqueda) |
            Q(nom_emp_soa__icontains=busqueda) |
            Q(fec_exp_soa__icontains=busqueda) |
            Q(fec_vig_soa__icontains=busqueda) |
            Q(fec_ven_soa__icontains=busqueda) 
            )
            datos = {'soats': res_busqueda}
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            return render(request, "crud_soat/listar.html", datos)
        else:
            datos = { 'soats' : lista }
            return render(request, "crud_soat/listar.html", datos)
    else:
        soats = Soat.objects.order_by('-id_soa')[:10]
        datos = { 'soats' : soats }
        return render(request, "crud_soat/listar.html", datos)

def agregarsoa(request):
    if request.method == 'POST':
        if request.POST.get('nom_emp_soa') and request.POST.get('fec_exp_soa'):
            if request.POST.get('fec_ven_soa') > request.POST.get('fec_exp_soa'):
            
                soat = Soat()
                soat.id_soa = request.POST.get('id_soa')
                soat.nom_emp_soa = request.POST.get('nom_emp_soa')
                soat.fec_exp_soa = request.POST.get('fec_exp_soa')
                soat.fec_vig_soa = request.POST.get('fec_vig_soa')
                soat.fec_ven_soa = request.POST.get('fec_ven_soa')
                soat.save()
                messages.success(request, 'El SOAT de {} fue agregado'.format(soat.nom_emp_soa))
                return redirect('listarsoa')
            else:
                messages.warning(request, 'La fecha de expedición es mayor a la de vencimiento.')
                return redirect('agregarsoa')
    else:
        soats = Soat.objects.all()
        datos = {'dependencias' : soats}
        return render(request,"crud_soat/agregar.html",datos)

def actualizarsoa(request, idSoat):
    try:
        if request.method == 'POST':
            if request.POST.get('nom_emp_soa') and request.POST.get('fec_exp_soa'):
                if request.POST.get('fec_ven_soa') > request.POST.get('fec_exp_soa'):
            
                    soat = Soat()
                    soat.id_soa = request.POST.get('id')
                    soat.nom_emp_soa = request.POST.get('nom_emp_soa')
                    soat.fec_exp_soa = request.POST.get('fec_exp_soa')
                    soat.fec_vig_soa = request.POST.get('fec_vig_soa')
                    soat.fec_ven_soa = request.POST.get('fec_ven_soa')
                    soat.save()
                    messages.success(request, 'El SOAT de {} fue modificado'.format(soat.nom_emp_soa))
                    return redirect('listarsoa')
                else:
                    messages.error(request, 'La fecha de expedición es mayor a la de vencimiento.')
                    return redirect('agregarsoa')
        else:
            soat = Soat.objects.get( id_soa=idSoat )
            soat.fec_exp_soa = date.strftime(soat.fec_exp_soa, "%Y-%m-%d")
            soat.fec_vig_soa = date.strftime(soat.fec_vig_soa, "%Y-%m-%d")
            soat.fec_ven_soa = date.strftime(soat.fec_ven_soa, "%Y-%m-%d")
            soats = Soat.objects.all()
            datos = {'soats' : soats, 'soat' : soat }
            return render(request,"crud_soat/actualizar.html",datos)
    except Soat.DoesNotExist:
        soat = None
        soats = Soat.objects.all()
        datos = {'soats' : soats, 'soat' : soat }
        return render(request,"crud_soat/actualizar.html",datos)

def eliminarsoa(request, idSoat):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar= request.POST.get('id')
                tupla=Soat.objects.get(id_soa = id_a_borrar)
                tupla.delete()
                messages.success(request, 'El SOAT de {} fue eliminado'.format(tupla.nom_emp_soa))
                return redirect('listarsoa')
        else:
            soats = Soat.objects.all()
            soat = Soat.objects.get( id_soa=idSoat )
            datos = {'soats' : soats, 'soat' : soat }
            return render(request,"crud_soat/eliminar.html",datos)
    except Soat.DoesNotExist:
        soat = None
        soats = Soat.objects.all()
        datos = {'soats' : soats, 'soat' : soat }
        return render(request,"crud_soat/eliminar.html",datos)
    
def listartec(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Tecnicomecanica.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_tec__icontains=busqueda) |
            Q(nom_emp_tec__icontains=busqueda) |
            Q(fec_exp_tec__icontains=busqueda) |
            Q(fec_ven_tec__icontains=busqueda) 
            )
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            datos = {'tecs': res_busqueda}
            return render(request, "crud_tecno/listar.html", datos)
        else:
            datos = { 'tecs' : lista }
            return render(request, "crud_tecno/listar.html", datos)
    else:
        tecs = Tecnicomecanica.objects.order_by('-id_tec')[:10]
        datos = { 'tecs' : tecs }
        return render(request, "crud_tecno/listar.html", datos)

def agregartec(request):
    if request.method == 'POST':
        if request.POST.get('nom_emp_tec') and request.POST.get('fec_exp_tec'):
            if request.POST.get('fec_ven_tec') > request.POST.get('fec_exp_tec'):
                tec = Tecnicomecanica()
                tec.id_tec = request.POST.get('id_tec')
                tec.nom_emp_tec = request.POST.get('nom_emp_tec')
                tec.fec_exp_tec = request.POST.get('fec_exp_tec')
                tec.fec_ven_tec = request.POST.get('fec_ven_tec')
                tec.save()
                messages.success(request, 'La técnico mecánica de {} fue agregada'.format(tec.nom_emp_tec))
                return redirect('listartec')
            else:
                messages.warning(request, 'La fecha de expedición es mayor a la de vencimiento.')
                return redirect('agregartec')
    else:
        tecs = Tecnicomecanica.objects.all()
        datos = {'tecs' : tecs}
        return render(request,"crud_tecno/agregar.html",datos)

def actualizartec(request, idTecno):
    try:
        if request.method == 'POST':
            if request.POST.get('nom_emp_tec') and request.POST.get('fec_exp_tec'):
                if request.POST.get('fec_ven_tec') > request.POST.get('fec_exp_tec'):
                    tec = Tecnicomecanica()
                    tec.id_tec = request.POST.get('id')
                    tec.nom_emp_tec = request.POST.get('nom_emp_tec')
                    tec.fec_exp_tec = request.POST.get('fec_exp_tec')
                    tec.fec_ven_tec = request.POST.get('fec_ven_tec')
                    tec.save()
                    messages.success(request, 'La técnico mecánica de {} fue modificada'.format(tec.nom_emp_tec))
                    return redirect('listartec')
                else:
                    messages.error(request, 'La fecha de expedición es mayor a la de vencimiento.')
                    return redirect('agregartec')
        else:
            tec = Tecnicomecanica.objects.get( id_tec=idTecno )
            tec.fec_exp_tec = date.strftime(tec.fec_exp_tec, "%Y-%m-%d")
            tec.fec_ven_tec = date.strftime(tec.fec_ven_tec, "%Y-%m-%d")
            tecs = Tecnicomecanica.objects.all()
            datos = {'tecs' : tecs, 'tec' : tec }
            return render(request,"crud_tecno/actualizar.html",datos)
    except Tecnicomecanica.DoesNotExist:
        tec = None
        tecs = Tecnicomecanica.objects.all()
        datos = {'tecs' : tecs, 'tec' : tec }
        return render(request,"crud_tecno/actualizar.html",datos)

def eliminartec(request, idTecno):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar= request.POST.get('id')
                tupla=Tecnicomecanica.objects.get(id_tec = id_a_borrar)
                tupla.delete()
                messages.success(request, 'La técnico mecánica de {} fue eliminada'.format(tupla.nom_emp_tec))
                return redirect('listartec')
        else:
            tec = Tecnicomecanica.objects.get( id_tec=idTecno )
            tecs = Tecnicomecanica.objects.all()
            datos = {'tecs' : tecs, 'tec' : tec }
            return render(request,"crud_tecno/eliminar.html",datos)
    except Tecnicomecanica.DoesNotExist:
        tec = None
        tecs = Tecnicomecanica.objects.all()
        datos = {'tecs' : tecs, 'tec' : tec }
        return render(request,"crud_tecno/eliminar.html",datos)
    
def listarasi(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = VehiculosAsignados.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id__icontains=busqueda) |
            Q(fec_ing__icontains=busqueda) |
            Q(fec_sal__icontains=busqueda) |
            Q(obs_veh_asi__icontains=busqueda)|
            Q(id_per=busqueda)|
            Q(id_veh=busqueda)
            )
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            datos = {'asis': res_busqueda}
            return render(request, "crud_asignaciones/listar.html", datos)
        else:
            datos = { 'asis' : lista }
            return render(request, "crud_asignaciones/listar.html", datos)
    else:
        asis = VehiculosAsignados.objects.order_by('-id')[:10]
        users = Usuarios.objects.all()
        datos = { 'asignaciones' : asis, 'usuarios': users}
        return render(request, "crud_asignaciones/listar.html", datos)

def agregarasi(request):
    if request.method == 'POST':
        if request.POST.get('id_per') and request.POST.get('id_veh'):
            veh = Vehiculos.objects.get( pla_veh= request.POST.get('id_veh'))
            asi = VehiculosAsignados()
            asi.id_per_id = request.POST.get('id_per')
            asi.id_veh_id = request.POST.get('id_veh')
            asi.fec_sal = request.POST.get('fec_sal')
            asi.obs_veh_asi = request.POST.get('obs_asi')
            asi.save()
            veh.est_veh = False
            veh.save()
            messages.success(request, 'Vehiculo de placas {} asignado al usuario {}'.format(asi.id_veh_id,asi.id_per_id))
            return redirect('listarasi')
    else:
        asis = VehiculosAsignados.objects.all()
        users = Usuarios.objects.all()
        vehs = Vehiculos.objects.all()
        datos = {'asis' : asis, 'usuarios': users, 'vehiculos': vehs}
        return render(request,"crud_asignaciones/agregar.html",datos)

def actualizarasi(request, idAsignacion):
    try:
        if request.method == 'POST':
            if request.POST.get('id_per') and request.POST.get('id_veh'):
                
                asi_id_old = request.POST.get('id')
                asi_old = VehiculosAsignados()
                asi_old = VehiculosAsignados.objects.get( id=asi_id_old )
                if( asi_old.fec_sal < request.POST.get('fec_sal')):
                    asi = VehiculosAsignados()
                    asi.id = request.POST.get('id')
                    asi.id_per_id = request.POST.get('id_per')
                    asi.id_veh_id = request.POST.get('id_veh')
                    asi.fec_ing = asi_old.fec_ing
                    asi.fec_sal = request.POST.get('fec_sal')
                    asi.obs_veh_asi = request.POST.get('obs_asi')
                    asi.save()
                    messages.success(request, 'La asignacion {} fue modificada'.format(asi.id))
                    return redirect('listarasi')
                else:
                    messages.warning(request, 'La fecha de ingreso es mayor a la de finalización.')
                    return redirect('actualizarasi')
        else:
            asi = VehiculosAsignados.objects.get( id=idAsignacion )
            asi.fec_sal = date.strftime(asi.fec_sal, "%Y-%m-%d %H:%M")
            asis = VehiculosAsignados.objects.all()
            users = Usuarios.objects.all()
            vehs = Vehiculos.objects.all()
            datos = {'asis' : asis, 'asi' : asi, 'usuarios': users, 'vehiculos': vehs}
            return render(request,"crud_asignaciones/actualizar.html",datos)
    except VehiculosAsignados.DoesNotExist:
        asi = None
        asis = VehiculosAsignados.objects.all()
        users = Usuarios.objects.all()
        vehs = Vehiculos.objects.all()
        datos = {'asis' : asis, 'asi' : asi, 'usuarios': users, 'vehiculos': vehs} 
        return render(request,"crud_asignaciones/actualizar.html",datos)

def eliminarasi(request, idAsignacion):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                id_a_borrar= request.POST.get('id')
                
                tupla=VehiculosAsignados.objects.get(id = id_a_borrar)
                veh = Vehiculos.objects.get( pla_veh = tupla.id_veh_id )
                veh.est_veh = True
                tupla.delete()
                veh.save()
                messages.warning(request, 'La asignación {} fue eliminada.'.format(tupla.id))
                return redirect('listarasi')
        else:
            asi = VehiculosAsignados.objects.get( id=idAsignacion )
            asis = VehiculosAsignados.objects.all()
            datos = {'asis' : asis, 'asi' : asi }
            return render(request,"crud_asignaciones/eliminar.html",datos)
    except VehiculosAsignados.DoesNotExist:
        asi = None
        asis = VehiculosAsignados.objects.all()
        datos = {'asis' : asis, 'asi' : asi }
        return render(request,"crud_asignaciones/eliminar.html",datos)

def listarprem(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Preoperacionalesm.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_pre__icontains=busqueda) |
            Q(fec_pre__icontains=busqueda) |
            Q(pla_pre=busqueda)
            )
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            datos = {'prems': res_busqueda}
            return render(request, "revisiones/preoperacionales/moto/listar.html", datos)
        else:
            datos = { 'prems' : lista }
            return render(request, "revisiones/preoperacionales/moto/listar.html", datos)
    else:
        prems = Preoperacionalesm.objects.order_by('-id_pre')[:10]

        datos = { 'prems' : prems}
        return render(request, "revisiones/preoperacionales/moto/listar.html", datos)
    
def agregarprem(request):
    if request.method == 'POST':
        if request.POST.get('pla_pre'):
            try:
                prem = Preoperacionalesm()
                prem.niv_pre = request.POST.get('niv_pre')
                prem.man_pre = request.POST.get('man_pre')
                prem.dir_pre = request.POST.get('dir_pre')
                prem.gua_pre = request.POST.get('gua_pre')
                prem.cha_pre = request.POST.get('cha_pre')
                prem.sus_pre = request.POST.get('sus_pre')
                prem.fre_pre = request.POST.get('fre_pre')
                prem.lla_pre = request.POST.get('lla_pre')
                prem.rin_pre = request.POST.get('rin_pre')
                prem.tre_pre = request.POST.get('tre_pre')
                prem.exo_pre = request.POST.get('exo_pre')
                prem.ret_pre = request.POST.get('ret_pre')
                prem.man_mec_pre = request.POST.get('man_mec_pre')
                prem.luc_pre = request.POST.get('luc_pre')
                prem.dir_stop_pre = request.POST.get('dir_stop_pre')
                prem.pit_pre = request.POST.get('pit_pre')
                prem.obs_pre = request.POST.get('obs_pre')
                prem.fec_pre = request.POST.get('fec_pre')
                prem.pla_pre_id = request.POST.get('pla_pre')
                prem.save()
                messages.success(request, 'La asignación quedo registrada con el id {} sastifactoriamente'.format(prem.id_pre))
                return redirect('listarprem')
            except:
                messages.error(request, 'La placa de la moto {} no existe'.format(prem.pla_pre_id))
                return redirect('agregarprem')
    else:
        prems = Preoperacionalesm.objects.all()
        datos = { 'prems' : prems}
        return render(request, "revisiones/preoperacionales/moto/agregar.html", datos)
    return render(request, "revisiones/preoperacionales/moto/agregar.html")

def actualizarprem(request, idprem):
    try:
        if request.method == 'POST':
            if request.POST.get('id_pre'):
                asi_id_old = request.POST.get('id_pre')
                asi_old = Preoperacionalesm()
                asi_old = Preoperacionalesm.objects.get( id_pre=asi_id_old )
                prem = Preoperacionalesm()
                prem.id_pre = request.POST.get('id_pre')
                prem.niv_pre = request.POST.get('niv_pre')
                prem.man_pre = request.POST.get('man_pre')
                prem.dir_pre = request.POST.get('dir_pre')
                prem.gua_pre = request.POST.get('gua_pre')
                prem.cha_pre = request.POST.get('cha_pre')
                prem.sus_pre = request.POST.get('sus_pre')
                prem.fre_pre = request.POST.get('fre_pre')
                prem.lla_pre = request.POST.get('lla_pre')
                prem.rin_pre = request.POST.get('rin_pre')
                prem.tre_pre = request.POST.get('tre_pre')
                prem.exo_pre = request.POST.get('exo_pre')
                prem.ret_pre = request.POST.get('ret_pre')
                prem.man_mec_pre = request.POST.get('man_mec_pre')
                prem.luc_pre = request.POST.get('luc_pre')
                prem.dir_stop_pre = request.POST.get('dir_stop_pre')
                prem.pit_pre = request.POST.get('pit_pre')
                prem.obs_pre = request.POST.get('obs_pre')
                prem.fec_pre = asi_old.fec_pre
                prem.pla_pre_id = request.POST.get('pla_pre')
                prem.save()
                messages.success(request, 'La revisión preoperacional con el id {} fue modificada'.format(prem.id_pre))
                return redirect('listarprem')
        else:
            prem = Preoperacionalesm.objects.get( id_pre=idprem )
            prems = Preoperacionalesm.objects.all()
            datos = {'prems' : prems, 'prem' : prem }
            return render(request,"revisiones/preoperacionales/moto/actualizar.html",datos)
    except Preoperacionalesm.DoesNotExist:
        prem = None
        prems = Preoperacionalesm.objects.all()
        datos = {'prems' : prems, 'prem' : prem }
        return render(request,"revisiones/preoperacionales/moto/actualizar.html",datos)

def eliminarprem(request, idprem):   
    try:
            if request.method=='POST':
                if request.POST.get('id_pre'):
                    id_a_borrar= request.POST.get('id_pre')
                    
                    tupla=Preoperacionalesm.objects.get(id_pre = id_a_borrar)
                    messages.warning(request, 'La revisión preoperacional con el id {} fue eliminada.'.format(tupla.id_pre))
                    tupla.delete()
                    
                    return redirect('listarprem')
            else:
                prem = Preoperacionalesm.objects.get( id_pre=idprem )
            prems = Preoperacionalesm.objects.all()
            datos = {'prems' : prems, 'prem' : prem }
            return render(request,"revisiones/preoperacionales/moto/eliminar.html",datos)
    except Preoperacionalesm.DoesNotExist:
        prem = None
        prems = Preoperacionalesm.objects.all()
        datos = {'prems' : prems, 'prem' : prem }
        return render(request,"revisiones/preoperacionales/moto/eliminar.html",datos)

def listarprec(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Preoperacionalesc.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_pre__icontains=busqueda) |
            Q(fec_pre__icontains=busqueda) |
            Q(pla_pre=busqueda)
            )
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            datos = {'precs': res_busqueda}
            return render(request, "revisiones/preoperacionales/carro/listar.html", datos)
        else:
            datos = { 'precs' : lista }
            return render(request, "revisiones/preoperacionales/carro/listar.html", datos)
    else:
        precs = Preoperacionalesc.objects.order_by('-id_pre')[:10]

        datos = { 'precs' : precs}
        return render(request, "revisiones/preoperacionales/carro/listar.html", datos)
    
def agregarprec(request):
    if request.method == 'POST':
        if request.POST.get('pla_pre'):
            try:
                prec = Preoperacionalesc()
                prec.dir_del_pre = request.POST.get('dir_del_pre')
                prec.dir_tra_pre = request.POST.get('dir_tra_pre')
                prec.sis_luc_pre = request.POST.get('sis_luc_pre')
                prec.luc_fre_pre = request.POST.get('luc_fre_pre')
                prec.luc_rev_pre = request.POST.get('luc_rev_pre')
                prec.luc_par_pre = request.POST.get('luc_par_pre')
                prec.vpan_pre = request.POST.get('vpan_pre')
                prec.vlat_pre = request.POST.get('vlat_pre')
                prec.vtra_pre = request.POST.get('vtra_pre')
                prec.limp_pre = request.POST.get('limp_pre')
                prec.elat_pre = request.POST.get('elat_pre')
                prec.eret_pre = request.POST.get('eret_pre')
                prec.pit_pre = request.POST.get('pit_pre')
                prec.taco_pre = request.POST.get('taco_pre')
                prec.odo_pre = request.POST.get('odo_pre')
                prec.gas_pre = request.POST.get('gas_pre')
                prec.tem_pre = request.POST.get('tem_pre')
                prec.cin_pre = request.POST.get('cin_pre')
                prec.alar_pre = request.POST.get('alar_pre')
                prec.cha_pue_pre = request.POST.get('cha_pue_pre')
                prec.pue_cie_pre = request.POST.get('pue_cie_pre')
                prec.esc_acc_pre = request.POST.get('esc_acc_pre')
                prec.pas_tec_pre = request.POST.get('pas_tec_pre')
                prec.ven_eme_pre = request.POST.get('ven_eme_pre')
                prec.alc_vol_pre = request.POST.get('alc_vol_pre')
                prec.fre_pri_pre = request.POST.get('fre_pri_pre')
                prec.fre_man_pre = request.POST.get('fre_man_pre')
                prec.agu_lim_pre = request.POST.get('agu_lim_pre')
                prec.agu_ref_pre = request.POST.get('agu_ref_pre')
                prec.ace_mot_pre = request.POST.get('ace_mot_pre')
                prec.liq_fre_pre = request.POST.get('liq_fre_pre')
                prec.liq_bat_pre = request.POST.get('liq_bat_pre')
                prec.ace_hid_pre = request.POST.get('ace_hid_pre')
                prec.cor_pre = request.POST.get('cor_pre')
                prec.man_pre = request.POST.get('man_pre')
                prec.est_lla_pre = request.POST.get('est_lla_pre')
                prec.pre_lla_pre = request.POST.get('pre_lla_pre')
                prec.lab_lla_pre = request.POST.get('lab_lla_pre')
                prec.rep_lla_pre = request.POST.get('rep_lla_pre')
                prec.señ_eme_pre = request.POST.get('señ_eme_pre')
                prec.tac_pre = request.POST.get('tac_pre')
                prec.cha_pre = request.POST.get('cha_pre')
                prec.gat_pre = request.POST.get('gat_pre')
                prec.gua_pre = request.POST.get('gua_pre')
                prec.cru_pre = request.POST.get('cru_pre')
                prec.her_pre = request.POST.get('her_pre')
                prec.bot_pre = request.POST.get('bot_pre')
                prec.ext_pre = request.POST.get('ext_pre')
                prec.obs_pre = request.POST.get('obs_pre')
                prec.fec_pre = request.POST.get('fec_pre')
                prec.pla_pre_id = request.POST.get('pla_pre')
                prec.save()
                messages.success(request, 'La asignación quedo registrada con el id {} sastifactoriamente'.format(prec.id_pre))
                return redirect('listarprec')
            except:
                messages.error(request, 'La placa del vehiculo {} no existe'.format(prec.pla_pre_id))
                return redirect('agregarprec')
    else:
        prems = Preoperacionalesm.objects.all()
        datos = { 'prems' : prems}
        return render(request, "revisiones/preoperacionales/carro/agregar.html", datos)

def actualizarprec(request, idprec):
    try:
        if request.method == 'POST':
            if request.POST.get('id_pre'):
                asi_id_old = request.POST.get('id_pre')
                asi_old = Preoperacionalesc()
                asi_old = Preoperacionalesc.objects.get( id_pre=asi_id_old )
                prec = Preoperacionalesc()
                prec.id_pre = request.POST.get('id_pre')
                prec.dir_del_pre = request.POST.get('dir_del_pre')
                prec.dir_tra_pre = request.POST.get('dir_tra_pre')
                prec.sis_luc_pre = request.POST.get('sis_luc_pre')
                prec.luc_fre_pre = request.POST.get('luc_fre_pre')
                prec.luc_rev_pre = request.POST.get('luc_rev_pre')
                prec.luc_par_pre = request.POST.get('luc_par_pre')
                prec.vpan_pre = request.POST.get('vpan_pre')
                prec.vlat_pre = request.POST.get('vlat_pre')
                prec.vtra_pre = request.POST.get('vtra_pre')
                prec.limp_pre = request.POST.get('limp_pre')
                prec.elat_pre = request.POST.get('elat_pre')
                prec.eret_pre = request.POST.get('eret_pre')
                prec.pit_pre = request.POST.get('pit_pre')
                prec.taco_pre = request.POST.get('taco_pre')
                prec.odo_pre = request.POST.get('odo_pre')
                prec.gas_pre = request.POST.get('gas_pre')
                prec.tem_pre = request.POST.get('tem_pre')
                prec.cin_pre = request.POST.get('cin_pre')
                prec.alar_pre = request.POST.get('alar_pre')
                prec.cha_pue_pre = request.POST.get('cha_pue_pre')
                prec.pue_cie_pre = request.POST.get('pue_cie_pre')
                prec.esc_acc_pre = request.POST.get('esc_acc_pre')
                prec.pas_tec_pre = request.POST.get('pas_tec_pre')
                prec.ven_eme_pre = request.POST.get('ven_eme_pre')
                prec.alc_vol_pre = request.POST.get('alc_vol_pre')
                prec.fre_pri_pre = request.POST.get('fre_pri_pre')
                prec.fre_man_pre = request.POST.get('fre_man_pre')
                prec.agu_lim_pre = request.POST.get('agu_lim_pre')
                prec.agu_ref_pre = request.POST.get('agu_ref_pre')
                prec.ace_mot_pre = request.POST.get('ace_mot_pre')
                prec.liq_fre_pre = request.POST.get('liq_fre_pre')
                prec.liq_bat_pre = request.POST.get('liq_bat_pre')
                prec.ace_hid_pre = request.POST.get('ace_hid_pre')
                prec.cor_pre = request.POST.get('cor_pre')
                prec.man_pre = request.POST.get('man_pre')
                prec.est_lla_pre = request.POST.get('est_lla_pre')
                prec.pre_lla_pre = request.POST.get('pre_lla_pre')
                prec.lab_lla_pre = request.POST.get('lab_lla_pre')
                prec.rep_lla_pre = request.POST.get('rep_lla_pre')
                prec.señ_eme_pre = request.POST.get('señ_eme_pre')
                prec.tac_pre = request.POST.get('tac_pre')
                prec.cha_pre = request.POST.get('cha_pre')
                prec.gat_pre = request.POST.get('gat_pre')
                prec.gua_pre = request.POST.get('gua_pre')
                prec.cru_pre = request.POST.get('cru_pre')
                prec.her_pre = request.POST.get('her_pre')
                prec.bot_pre = request.POST.get('bot_pre')
                prec.ext_pre = request.POST.get('ext_pre')
                prec.obs_pre = request.POST.get('obs_pre')
                prec.fec_pre = asi_old.fec_pre
                prec.pla_pre_id = request.POST.get('pla_pre')
                prec.save()
                messages.success(request, 'La revisión preoperacional con el id {} fue modificada'.format(prec.id_pre))
                return redirect('listarprec')
        else:
            prec = Preoperacionalesc.objects.get( id_pre=idprec )
            precs = Preoperacionalesc.objects.all()
            datos = {'precs' : precs, 'prec' : prec }
            return render(request,"revisiones/preoperacionales/carro/actualizar.html",datos)
    except Preoperacionalesc.DoesNotExist:
        prec = None
        precs = Preoperacionalesc.objects.all()
        datos = {'precs' : precs, 'prec' : prec }
        return render(request,"revisiones/preoperacionales/carro/actualizar.html",datos)

def eliminarprec(request, idprec):   
    try:
            if request.method=='POST':
                if request.POST.get('id_pre'):
                    id_a_borrar= request.POST.get('id_pre')
                    
                    tupla=Preoperacionalesc.objects.get(id_pre = id_a_borrar)
                    messages.warning(request, 'La revisión preoperacional con el id {} fue eliminada.'.format(tupla.id_pre))
                    tupla.delete()
                    
                    return redirect('listarprec')
            else:
                prec = Preoperacionalesc.objects.get( id_pre = idprec )
                precs = Preoperacionalesc.objects.all()
                datos = {'precs' : precs, 'prec' : prec }
                return render(request,"revisiones/preoperacionales/carro/eliminar.html",datos)
    except Preoperacionalesm.DoesNotExist:
        prec = None
        precs = Preoperacionalesc.objects.all()
        datos = {'precs' : precs, 'prec' : prec }
        return render(request,"revisiones/preoperacionales/carro/eliminar.html",datos)

def listarman(request):

    if request.method == 'POST':
        busqueda = request.POST.get('keyword')
        lista = Mantenimiento.objects.all()

        if busqueda is not None:
            res_busqueda = lista.filter(
            Q(id_man__icontains=busqueda) |
            Q(id_veh=busqueda) |
            Q(fec_man__icontains=busqueda) |
            Q(per_man__icontains=busqueda) |
            Q(tipo_man__icontains=busqueda)
            )
            messages.success(request, 'Resultados encontrados por: {}'.format(busqueda))
            datos = {'mans': res_busqueda}
            return render(request, "revisiones/mantenimiento/listar.html", datos)
        else:
            datos = { 'mans' : lista }
            return render(request, "revisiones/mantenimiento/listar.html", datos)
    else:
        mans = Mantenimiento.objects.order_by('-id_man')[:10]
        datos = { 'mans' : mans}
        return render(request, "revisiones/mantenimiento/listar.html", datos)

def agregarman(request):
    if request.method == 'POST':
        if request.POST.get('id_veh'):
            try:
                man = Mantenimiento()
                man.fec_man = request.POST.get('fec_man')
                man.tipo_man = request.POST.get('tipo_man')
                man.des_obs_man = request.POST.get('des_obs_man')
                man.per_man = request.POST.get('per_man')
                man.rec_man = request.POST.get('rec_man')
                man.id_veh_id = request.POST.get('id_veh')
                man.save()
                messages.success(request, 'El mantenimiendo se registro con el id {} sastifactoriamente'.format(man.id_man))
                return redirect('listarman')
            except:
                messages.error(request, 'La placa del vehiculo {} no existe'.format(man.id_veh_id))
                return redirect('agregarman')
    else:
        mans = Mantenimiento.objects.all()
        datos = { 'mans' : mans}
        return render(request, "revisiones/mantenimiento/agregar.html", datos)

def actualizarman(request, idman):
    try:
        if request.method == 'POST':
            if request.POST.get('id_man'):
                man = Mantenimiento()
                man.id_man = request.POST.get('id_man')
                man.fec_man = request.POST.get('fec_man')
                man.tipo_man = request.POST.get('tipo_man')
                man.des_obs_man = request.POST.get('des_obs_man')
                man.per_man = request.POST.get('per_man')
                man.rec_man = request.POST.get('rec_man')
                man.id_veh_id = request.POST.get('id_veh')
                man.save()
                messages.success(request, 'El mantenimiento con el id {} fue modificado'.format(man.id_man))
                return redirect('listarman')
        else:
            man = Mantenimiento.objects.get( id_man=idman )
            man.fec_man = date.strftime(man.fec_man, "%Y-%m-%d")
            mans = Mantenimiento.objects.all()
            datos = {'mans' : mans, 'man' : man }
            return render(request,"revisiones/mantenimiento/actualizar.html",datos)
    except Mantenimiento.DoesNotExist:
        man = None
        mans = Mantenimiento.objects.all()
        datos = {'mans' : mans, 'man' : man }
        return render(request,"revisiones/mantenimiento/actualizar.html",datos)

def eliminarman(request, idman):   
    try:
            if request.method=='POST':
                if request.POST.get('id_man'):
                    id_a_borrar= request.POST.get('id_man')
                    
                    tupla=Mantenimiento.objects.get(id_man = id_a_borrar)
                    messages.warning(request, 'La revisión preoperacional con el id {} fue eliminada.'.format(tupla.id_man))
                    tupla.delete()
                    
                    return redirect('listarman')
            else:
                man = Mantenimiento.objects.get( id_man = idman )
                mans = Mantenimiento.objects.all()
                datos = {'mans' : mans, 'man' : man }
                return render(request,"revisiones/mantenimiento/eliminar.html",datos)
    except Mantenimiento.DoesNotExist:
        man = None
        mans = Mantenimiento.objects.all()
        datos = {'mans' : mans, 'man' : man }
        return render(request,"revisiones/mantenimiento/eliminar.html",datos)