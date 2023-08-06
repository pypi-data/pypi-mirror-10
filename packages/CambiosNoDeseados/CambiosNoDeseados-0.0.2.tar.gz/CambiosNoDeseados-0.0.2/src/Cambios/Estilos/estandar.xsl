<?xml version='1.0' encoding='UTF-8'?>

<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

    <xsl:template match='/'>
        <html lang="es">
        <head>
            <meta charset='UTF-8'/>
            <base href='FILE:///home/wolfang/tee/'/>
            <link rel="stylesheet" type="text/css" href="Estilos/estandar.css"/>
            <title><xsl:value-of select='carta/nombre'/></title>
        </head>
        <body>
            <xsl:apply-templates select='carta'/>
        </body>
      </html>
    </xsl:template>

    <xsl:template match='carta'>

        <div class='cara' cara='imagen' subtipo='{@subtipo}'>
            <xsl:apply-templates select='imagen'/>
        </div>

        <div class='cara' cara='frente' tipo='{@tipo}' subtipo='{@subtipo}'>
            <div class='cabeza'>
                <div class='tipo'>
                    <xsl:choose>
                        <xsl:when test='@tipo = "Personaje"'>
                            <img src='Iconos/{peso}.png' alt='{peso}' class='icono' />
                        </xsl:when>
                        <xsl:when test='@tipo = "Recurso"'>
                            <img src='Iconos/{peso}.png' alt='{peso}' class='icono' />
                        </xsl:when>
                        <xsl:when test='@tipo = "Habilidad"'>
                            <img src='Iconos/{@subtipo}.png' alt='{@subtipo}' class='icono' />
                        </xsl:when>
                    </xsl:choose>
                </div>
                <div class='informacion'>
<!--
                    <xsl:if test='requerimientos'>
                        <div class='requerimientos'>
                            <xsl:apply-templates select='requerimientos' />
                        </div>
                    </xsl:if>
-->
                    <div class='nombre'>
                        <h1 class='titulo'><xsl:value-of select='nombre'/></h1>
                    </div>
                </div>
            </div>
            <div class='intermedio'>
                <div class='clases'>
                    <xsl:apply-templates select='clases'/>
                </div>
                <div class='vacio'>
<!--
                    <div class='artistas'>
                        <xsl:for-each select='imagen/artista'>
                            <span class='artista'>©<xsl:value-of select='.'/></span>
                        </xsl:for-each>
                    </div>
-->
                    <p class='historia'><xsl:value-of select='imagen/titulo'/></p>
                </div>
            </div>
            <div class='cuerpo'>
                <xsl:choose>
                    <xsl:when test='@tipo = "Recurso"'>
                        <div class='descripcion'>
                            <div class='tipo'>
                                <img class='icono' src='Iconos/{@subtipo}.png' alt='{@subtipo}'/>
                            </div>
                            <div class='valor'>
                                <img class='icono' src='Iconos/{valor}.png' alt='{valor}'/>
                            </div>
                        </div>
                    </xsl:when>
                    <xsl:when test='@tipo = "Personaje"'>
                        <xsl:apply-templates select='atributos'/>
                    </xsl:when>
                </xsl:choose>
                <xsl:apply-templates select='habilidad'/>
            </div>
            <div class='pie'>
                <xsl:apply-templates select='metadatos'/>
            </div>
        </div>

<!--
        <div class='cara' cara='fondo'>
            <div class='fondo'>
                <img src='Imagenes/Fondo.png' alt='{alternativo}' class='imagen' />
            </div>
            <div class='pie'>
                <span class='licencia'><xsl:value-of select='metadatos/@licencia'/></span>
            </div>
        </div>
-->

    </xsl:template>

<!--
    <xsl:template match='requerimientos'>
        <div class='region'>
            <p class='valor'>
                <xsl:choose>
                    <xsl:when test='region = ""'>
                        •
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select='region'/>
                    </xsl:otherwise>
                </xsl:choose>
            </p>
        </div>
        <div class='equipamento'>
            <p class='valor'>
                <xsl:choose>
                    <xsl:when test='equipamento = ""'>
                        •
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select='equipamento'/>
                    </xsl:otherwise>
                </xsl:choose>
            </p>
        </div>
    </xsl:template>
-->

    <xsl:template match='clases'>
        <div class='a'>
            <xsl:apply-templates select='clase'/>
        </div>
    </xsl:template>

    <xsl:template match='clase'>
        <div class='clase'>
            <img src='Iconos/{.}.png' alt='{.}' class='icono' />
        </div>
    </xsl:template>

    <xsl:template match='atributos'>
        <div class='atributos'>
            <div class='salud'>
                <img src='Iconos/Resistencia.png' alt='Salud' class='icono' />
                <img src='Iconos/{salud}.png' alt='{salud}' class='valor' />
            </div>
            <div class='consentracion'>
                <img src='Iconos/Energia.png' alt='consentración' class='icono' />
                <img src='Iconos/{consentracion}.png' alt='{consentracion}' class='valor' />
            </div>
            <div class='agilidad'>
                <img src='Iconos/Agilidad.png' alt='Movilidad' class='icono' />
                <img src='Iconos/{agilidad}.png' alt='{agilidad}' class='valor' />
            </div>
        </div>
    </xsl:template>

    <xsl:template match='habilidad'>
        <div class='habilidad'>
            <div class='titulo'>
                <h3 class='valor'><xsl:value-of select='titulo'/></h3>
            </div>
            <div class='cabeza'>
                <h4 class='activacion'><xsl:value-of select='activacion'/></h4>
                <div class='costo'>
                    <xsl:choose>
                        <xsl:when test='costo'>
                            <xsl:apply-templates select='costo'/>
                        </xsl:when>
                        <xsl:otherwise>&#160;•&#160;</xsl:otherwise>
                    </xsl:choose>
                </div>
            </div>
            <div class='cuerpo'>
                <div class='efecto'>
                    <xsl:apply-templates select='efecto'/>
                </div>
            </div>
            <div class='pie'>
                <xsl:apply-templates select='rango'/>
            </div>
        </div>
    </xsl:template>

    <xsl:template match='efecto'>
        <p class='valor'><xsl:apply-templates/></p>
    </xsl:template>

    <xsl:template match='costo'>
        &#160;
        <xsl:apply-templates />
        &#160;
    </xsl:template>

    <xsl:template match='rango'>
        <div class='afectados'>
            <span class='valor'><xsl:value-of select='forma/@afectados'/></span>
        </div>
        <div class='forma'>
            <span class='valor'><xsl:value-of select='forma/@cuadros'/></span>
        </div>
        <div class='alcanse'>
            <xsl:choose>
                <xsl:when test='alcanse'>
                    <xsl:apply-templates select='alcanse'/>
                </xsl:when>
                <xsl:otherwise>&#160;</xsl:otherwise>
            </xsl:choose>
        </div>
        <div class='radio'>
            <xsl:choose>
                <xsl:when test='radio'>
                    <xsl:apply-templates select='radio'/>
                </xsl:when>
                <xsl:otherwise>&#160;</xsl:otherwise>
            </xsl:choose>
        </div>
    </xsl:template>

    <xsl:template match='radio'>
        <span class='nombre'>R</span>
        <span class='valor'>
            <xsl:choose>
                <xsl:when test='@min = @max'>
                    <xsl:value-of select='@min'/>
                </xsl:when>
                <xsl:when test='@min = "1"'>
                    ~<xsl:value-of select='@max'/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:value-of select='@min'/>:<xsl:value-of select='@max'/>
                </xsl:otherwise>
            </xsl:choose>
        </span>
    </xsl:template>

    <xsl:template match='alcanse'>
        <h4 class='nombre'>A</h4>
        <span class='valor'>
            <xsl:choose>
                <xsl:when test='@min = @max'>
                    <xsl:value-of select='@min'/>
                </xsl:when>
                <xsl:when test='@min = "0"'>
                    ~<xsl:value-of select='@max'/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:value-of select='@min'/>:<xsl:value-of select='@max'/>
                </xsl:otherwise>
            </xsl:choose>
        </span>
    </xsl:template>

    <xsl:template match='token'>
        <div class='token'>
            <span class='valor'>
                <xsl:choose>
                    <xsl:when test='@min = @max'>
                        <xsl:value-of select='@valor'/>
                    </xsl:when>
                    <xsl:when test='@min = "0"'>
                        X~<xsl:value-of select='@max'/>
                    </xsl:when>
                    <xsl:when test='@min != @max'>
                        <xsl:value-of select='@min'/>:X:<xsl:value-of select='@max'/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select='@valor'/>
                    </xsl:otherwise>
                </xsl:choose>
            </span>
<!--
            <img src='Iconos/{@accion}.png' alt='{@accion}' class='accion' />
-->
            <img src='Iconos/{@tipo}.png' alt='{@tipo}' class='tipo'/>
        </div>
    </xsl:template>

    <xsl:template match='imagen'>
        <xsl:choose>
            <xsl:when test='@archivo'>
                <img src='Imagenes/{@archivo}' alt='{alternativo}' class='imagen' />
            </xsl:when>
            <xsl:otherwise>
                <img src='Imagenes/Fondo.png' alt='{alternativo}' class='imagen' />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template match='metadatos'>
        <div class='autor'>
            <span class='autores'>©</span>
            <xsl:for-each select='autor'>
                <span class='autores'><xsl:value-of select='.'/></span>
            </xsl:for-each>
        </div>
        <span class='serial'>#&#160;<xsl:value-of select='substring(/carta/@subtipo,1,1)'/><xsl:value-of select='serial'/>–<xsl:value-of select='vercion'/></span>
        <span class='temporada'>
            <xsl:value-of select='temporada'/>
        </span>
    </xsl:template>

</xsl:stylesheet>
