import pandas as pd;

from extractor import extraer_por_region_comuna



regiones_comunas = {
    "1": {"nombre": "DE TARAPACÁ", "id_region": "1", "comunas": {
        "1101": "IQUIQUE", "1107": "ALTO HOSPICIO", "1401": "POZO ALMONTE", "1402": "CAMIÑA", "1403": "COLCHANE", "1404": "HUARA", "1405": "PICA"
    }},
    "2": {"nombre": "DE ANTOFAGASTA", "id_region": "2", "comunas": {
        "2101": "ANTOFAGASTA", "2102": "MEJILLONES", "2103": "SIERRA GORDA", "2104": "TALTAL", "2201": "CALAMA", "2202": "OLLAGÜE",
        "2203": "SAN PEDRO DE ATACAMA", "2301": "TOCOPILLA", "2302": "MARÍA ELENA"
    }},
    "3": {"nombre": "DE ATACAMA", "id_region": "3", "comunas": {
        "3101": "COPIAPÓ", "3102": "CALDERA", "3103": "TIERRA AMARILLA", "3201": "CHAÑARAL", "3202": "DIEGO DE ALMAGRO",
        "3301": "VALLENAR", "3302": "ALTO DEL CARMEN", "3303": "FREIRINA", "3304": "HUASCO"
    }},
    "4": {"nombre": "DE COQUIMBO", "id_region": "4", "comunas": {
        "4101": "LA SERENA", "4102": "COQUIMBO", "4103": "ANDACOLLO", "4104": "LA HIGUERA", "4105": "PAIGUANO", "4106": "VICUÑA",
        "4201": "ILLAPEL", "4202": "CANELA", "4203": "LOS VILOS", "4204": "SALAMANCA",
        "4301": "OVALLE", "4302": "COMBARBALÁ", "4303": "MONTE PATRIA", "4304": "PUNITAQUI", "4305": "RÍO HURTADO"
    }},
    "5": {"nombre": "DE VALPARAÍSO", "id_region": "5", "comunas": {
        "5101": "VALPARAÍSO", "5102": "CASABLANCA", "5103": "CONCÓN", "5104": "JUAN FERNÁNDEZ", "5105": "PUCHUNCAVÍ", "5107": "QUINTERO", "5109": "VIÑA DEL MAR",
        "5201": "ISLA DE PASCUA",
        "5301": "LOS ANDES", "5302": "CALLE LARGA", "5303": "RINCONADA", "5304": "SAN ESTEBAN",
        "5401": "LA LIGUA", "5402": "CABILDO", "5403": "PAPUDO", "5404": "PETORCA", "5405": "ZAPALLAR",
        "5501": "QUILLOTA", "5502": "LA CALERA", "5503": "HIJUELAS", "5504": "LA CRUZ", "5506": "NOGALES",
        "5601": "SAN ANTONIO", "5602": "ALGARROBO", "5603": "CARTAGENA", "5604": "EL QUISCO", "5605": "EL TABO", "5606": "SANTO DOMINGO",
        "5701": "SAN FELIPE", "5702": "CATEMU", "5703": "LLAILLAY", "5704": "PANQUEHUE", "5705": "PUTAENDO", "5706": "SANTA MARÍA",
        "5801": "QUILPUÉ", "5802": "LIMACHE", "5803": "OLMUÉ", "5804": "VILLA ALEMANA"
    }},
    "6": {"nombre": "DEL LIBERTADOR BERNARDO OHIGGINS", "id_region": "6", "comunas": {
        "6101": "RANCAGUA", "6102": "CODEGUA", "6103": "COINCO", "6104": "COLTAUCO", "6105": "DOÑIHUE", "6106": "GRANEROS", "6107": "LAS CABRAS",
        "6108": "MACHALÍ", "6109": "MALLOA", "6110": "MOSTAZAL", "6111": "OLIVAR", "6112": "PEUMO", "6113": "PICHIDEGUA", "6114": "QUINTA DE TILCOCO",
        "6115": "RENGO", "6116": "REQUÍNOA", "6117": "SAN VICENTE",
        "6201": "PICHILEMU", "6202": "LA ESTRELLA", "6203": "LITUECHE", "6204": "MARCHIHUE", "6205": "NAVIDAD", "6206": "PAREDONES",
        "6301": "SAN FERNANDO", "6302": "CHÉPICA", "6303": "CHIMBARONGO", "6304": "LOLOL", "6305": "NANCAGUA", "6306": "PALMILLA", "6307": "PERALILLO",
        "6308": "PLACILLA", "6309": "PUMANQUE", "6310": "SANTA CRUZ"
    }},
    "7": {"nombre": "DEL MAULE", "id_region": "7", "comunas": {
        "7101": "TALCA", "7102": "CONSTITUCIÓN", "7103": "CUREPTO", "7104": "EMPEDRADO", "7105": "MAULE", "7106": "PELARCO", "7107": "PENCAHUE",
        "7108": "RÍO CLARO", "7109": "SAN CLEMENTE", "7110": "SAN RAFAEL",
        "7201": "CAUQUENES", "7202": "CHANCO", "7203": "PELLUHUE",
        "7301": "CURICÓ", "7302": "HUALAÑÉ", "7303": "LICANTÉN", "7304": "MOLINA", "7305": "RAUCO", "7306": "ROMERAL", "7307": "SAGRADA FAMILIA",
        "7308": "TENO", "7309": "VICHUQUÉN",
        "7401": "LINARES", "7402": "COLBÚN", "7403": "LONGAVÍ", "7404": "PARRAL", "7405": "RETIRO", "7406": "SAN JAVIER", "7407": "VILLA ALEGRE",
        "7408": "YERBAS BUENAS"
    }},
    "8": {"nombre": "DEL BIOBÍO" , "id_region": "8", "comunas": {
        "8101": "CONCEPCIÓN", "8102": "CORONEL", "8103": "CHIGUAYANTE", "8104": "FLORIDA", "8105": "HUALQUI", "8106": "LOTA", "8107": "PENCO",
        "8108": "SAN PEDRO DE LA PAZ", "8109": "SANTA JUANA", "8110": "TALCAHUANO", "8111": "TOMÉ", "8112": "HUALPÉN",
        "8201": "LEBU", "8202": "ARAUCO", "8203": "CAÑETE", "8204": "CONTULMO", "8205": "CURANILAHUE", "8206": "LOS ÁLAMOS", "8207": "TIRÚA",
        "8301": "LOS ÁNGELES", "8302": "ANTUCO", "8303": "CABRERO", "8304": "LAJA", "8305": "MULCHÉN", "8306": "NACIMIENTO", "8307": "NEGRETE",
        "8308": "QUILACO", "8309": "QUILLECO", "8310": "SAN ROSENDO", "8311": "SANTA BÁRBARA", "8312": "TUCAPEL", "8313": "YUMBEL", "8314": "ALTO BIOBÍO"
    }},
    "9": {"nombre": "DE LA ARAUCANÍA", "id_region": "9", "comunas": {
        "9101": "TEMUCO", "9102": "CARAHUE", "9103": "CUNCO", "9104": "CURARREHUE", "9105": "FREIRE", "9106": "GALVARINO",
        "9107": "GORBEA", "9108": "LAUTARO", "9109": "LONCOCHE", "9110": "MELIPEUCO", "9111": "NUEVA IMPERIAL",
        "9112": "PADRE LAS CASAS", "9113": "PERQUENCO", "9114": "PITRUFQUÉN", "9115": "PUCÓN", "9116": "SAAVEDRA",
        "9117": "TEODORO SCHMIDT", "9118": "TOLTÉN", "9119": "VILCÚN", "9120": "VILLARRICA", "9121": "CHOLCHOL",
        "9201": "ANGOL", "9202": "COLLIPULLI", "9203": "CURACAUTÍN", "9204": "ERCILLA", "9205": "LONQUIMAY",
        "9206": "LOS SAUCES", "9207": "LUMACO", "9208": "PURÉN", "9209": "RENAICO", "9210": "TRAIGUÉN", "9211": "VICTORIA"
    }},
    "10": {"nombre": "DE LOS LAGOS", "id_region": "10", "comunas": {
        "10101": "PUERTO MONTT", "10102": "CALBUCO", "10103": "COCHAMÓ", "10104": "FRESIA", "10105": "FRUTILLAR",
        "10106": "LOS MUERMOS", "10107": "LLANQUIHUE", "10108": "MAULLÍN", "10109": "PUERTO VARAS",
        "10201": "CASTRO", "10202": "ANCUD", "10203": "CHONCHI", "10204": "CURACO DE VÉLEZ", "10205": "DALCAHUE",
        "10206": "PUQUELDÓN", "10207": "QUEILÉN", "10208": "QUELLÓN", "10209": "QUEMCHI", "10210": "QUINCHAO",
        "10301": "OSORNO", "10302": "PUERTO OCTAY", "10303": "PURRANQUE", "10304": "PUYEHUE", "10305": "RÍO NEGRO",
        "10306": "SAN JUAN DE LA COSTA", "10307": "SAN PABLO",
        "10401": "CHAITÉN", "10402": "FUTALEUFÚ", "10403": "HUALAIHUÉ", "10404": "PALENA"
    }},
    "11": {"nombre": "DE AYSÉN DEL GENERAL CARLOS IBAÑEZ DEL CAMPO", "id_region": "11", "comunas": {
        "11101": "COYHAIQUE", "11102": "LAGO VERDE",
        "11201": "AYSÉN", "11202": "CISNES", "11203": "GUAITECAS",
        "11301": "COCHRANE", "11302": "O`HIGGINS", "11303": "TORTEL",
        "11401": "CHILE CHICO", "11402": "RÍO IBÁÑEZ"
    }},
    "12": {"nombre": "DE MAGALLANES Y DE LA ANTÁRTICA CHILENA", "id_region": "12", "comunas": {
        "12101": "PUNTA ARENAS", "12102": "LAGUNA BLANCA", "12103": "RÍO VERDE", "12104": "SAN GREGORIO",
        "12201": "CABO DE HORNOS", "12202": "ANTÁRTICA",
        "12301": "PORVENIR", "12302": "PRIMAVERA", "12303": "TIMAUKEL",
        "12401": "NATALES", "12402": "TORRES DEL PAINE"
    }},
    "13": {"nombre": "METROPOLITANA DE SANTIAGO", "id_region": "13", "comunas": {
        "13101": "SANTIAGO", "13102": "CERRILLOS", "13103": "CERRO NAVIA", "13104": "CONCHALÍ", "13105": "EL BOSQUE",
        "13106": "ESTACIÓN CENTRAL", "13107": "HUECHURABA", "13108": "INDEPENDENCIA", "13109": "LA CISTERNA",
        "13110": "LA FLORIDA", "13111": "LA GRANJA", "13112": "LA PINTANA", "13113": "LA REINA", "13114": "LAS CONDES",
        "13115": "LO BARNECHEA", "13116": "LO ESPEJO", "13117": "LO PRADO", "13118": "MACUL", "13119": "MAIPÚ",
        "13120": "ÑUÑOA", "13121": "PEDRO AGUIRRE CERDA", "13122": "PEÑALOLÉN", "13123": "PROVIDENCIA",
        "13124": "PUDAHUEL", "13125": "QUILICURA", "13126": "QUINTA NORMAL", "13127": "RECOLETA", "13128": "RENCA",
        "13129": "SAN JOAQUÍN", "13130": "SAN MIGUEL", "13131": "SAN RAMÓN", "13132": "VITACURA",
        "13201": "PUENTE ALTO", "13202": "PIRQUE", "13203": "SAN JOSÉ DE MAIPO",
        "13301": "COLINA", "13302": "LAMPA", "13303": "TILTIL",
        "13401": "SAN BERNARDO", "13402": "BUIN", "13403": "CALERA DE TANGO", "13404": "PAINE",
        "13501": "MELIPILLA", "13502": "ALHUÉ", "13503": "CURACAVÍ", "13504": "MARÍA PINTO", "13505": "SAN PEDRO",
        "13601": "TALAGANTE", "13602": "EL MONTE", "13603": "ISLA DE MAIPO", "13604": "PADRE HURTADO", "13605": "PEÑAFLOR"
    }},
    "14": {"nombre": "DE LOS RÍOS", "id_region": "14", "comunas": {
        "14101": "VALDIVIA", "14102": "CORRAL", "14103": "LANCO", "14104": "LOS LAGOS", "14105": "MÁFIL",
        "14106": "MARIQUINA", "14107": "PAILLACO", "14108": "PANGUIPULLI",
        "14201": "LA UNIÓN", "14202": "FUTRONO", "14203": "LAGO RANCO", "14204": "RÍO BUENO"
    }},
    "15": {"nombre": "DE ARICA Y PARINACOTA", "id_region": "15", "comunas": {
        "15101": "ARICA", "15102": "CAMARONES", "15201": "PUTRE", "15202": "GENERAL LAGOS"
    }},
    "16": {"nombre": "DE ÑUBLE", "id_region": "16", "comunas": {
        "16101": "CHILLÁN", "16102": "BULNES", "16301": "COBQUECURA", "16302": "COELEMU", "16201": "COIHUECO",
        "16103": "CHILLÁN VIEJO", "16104": "EL CARMEN", "16303": "NINHUE", "16202": "ÑIQUÉN", "16105": "PEMUCO",
        "16106": "PINTO", "16304": "PORTEZUELO", "16107": "QUILLÓN", "16305": "QUIRIHUE", "16306": "RÁNQUIL",
        "16203": "SAN CARLOS", "16204": "SAN FABIÁN", "16108": "SAN IGNACIO", "16205": "SAN NICOLÁS",
        "16307": "TREGUACO", "16109": "YUNGAY"
    }}
}

todos_los_resultados = []

for region_id, region_data in regiones_comunas.items():
    for comuna_id, comuna_nombre in region_data["comunas"].items():
        print(f"Consultando: Región {region_data['nombre']} ({region_data['id_region']}), Comuna {comuna_nombre} ({comuna_id})")
        resultados = extraer_por_region_comuna(region_data["id_region"],comuna_id,region_data['nombre'],comuna_nombre)
        todos_los_resultados.extend(resultados)



        # Aquí iría tu request con `payload`


df = pd.DataFrame(todos_los_resultados)
df.to_csv("establecimientos_iquique.csv", index=False, encoding='utf-8-sig')
print(" Datos guardados en establecimientos_iquique.csv")
