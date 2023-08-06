CREATE OR ALTER TRIGGER SIC_DSCTO_VOLUMEN_MAX FOR DOCTOS_PV_DET
ACTIVE BEFORE INSERT OR UPDATE POSITION 0
AS
declare variable unidades_articulo double precision;
declare variable unidades_minimas double precision;
declare variable pctje_dscto_vol double precision;
declare variable diferencia double precision;
declare variable unidades_con_descuento double precision;
begin

/* VERIFICA QUE EL ARTICULO DEL DETALLE ACTUAL SE ENCUENTRE EN LA POLITICA DE SIC_VOLUMEN*/
if(exists(select * from dsctos_vol_arts dvo join  politicas_dsctos_volumen pvo on pvo.politica_dscto_volumen_id = dvo.politica_dscto_volumen_id
       where pvo.nombre = 'SIC_VOLUMEN' and dvo.articulo_id = new.articulo_id)) then
   begin
        /* REGRESA LAS UNIDADES Y EL PORCENTAJE DE DESCUENTO A APLICAR EN CADA CASO */
        select dvo.unidades, dvo.descuento from dsctos_vol_arts dvo join politicas_dsctos_volumen pvo on pvo.politica_dscto_volumen_id = dvo.politica_dscto_volumen_id
        where pvo.nombre = 'SIC_VOLUMEN' and dvo.articulo_id = new.articulo_id AND DVO.descuento > 0 into :unidades_minimas, :pctje_dscto_vol;
        
        /* SE OBTIENE LA CANTIDAD DE UNIDADES DEL MISMO ARTICULO EN LOS DEMAS DETALLES DEL DOCUMENTO */
        select sum(unidades) from doctos_pv_det dpd where dpd.articulo_id = new.articulo_id and dpd.docto_pv_id = new.docto_pv_id
        and dpd.docto_pv_det_id <> new.docto_pv_det_id into :unidades_articulo;
        
        /* VALIDACION SI NO HAY UNIDADES DE ARTICULO */
        if (unidades_articulo is null) then
        begin
            unidades_articulo = 0;
        end
        
        /* SOLO CUANDO LAS UNIDADES DE ARTICULOS SEAN MENORES QUE LAS DE LA POLITICA SE CAMBIARA EL DESCUENTO DEL DETALLE */
        if (unidades_articulo < unidades_minimas) then
        begin
            /* SI CON TODAS LAS UNIDADES NO SE ALCANZA LA CANTIDAD INDICADA EN LA POLITICA,
            SE APLICA EL DESCUENTO AL DETALLE EN TOTAL */
            if (unidades_minimas >= (new.unidades+unidades_articulo)) then
            begin
                new.pctje_dscto = pctje_dscto_vol;
            end
            /* SI SOLO UNA PARTE DE LAS UNIDADES REQUIERE DESCUENTO, ESTE SE CALCULA PARA LOGRAR EL EFECTO DE TENER EL DESCUENTO
             SOLO EN LAS UNIDADES INDICADAS EN LA POLITICA */
            else
            begin
                diferencia = unidades_articulo + new.unidades - unidades_minimas;
                unidades_con_descuento = new.unidades - diferencia;
                new.pctje_dscto = pctje_dscto_vol * unidades_con_descuento / new.unidades;
            end
        end
   end
end