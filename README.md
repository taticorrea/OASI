## Observatório Nacional

Repositório com scripts para o processo de redução de imagem e fotometria com o pacote IRAF e alguns scripts em python para análise de dados.

Created repository for store image reduction process and photometry scripts with IRAF package and some scripts in python for data analysis.


## Comandos cl usados

For image reduction process with IRAF package the following commands were used:

imarith

- !ls (criar lista em um arquivo .txt com imagens)
- imarit  (operações aritiméticas entre imagens)
- imcombine nomedaimagem.fit (combinar imagens)
- imstat nomedaimagem.fit[regiao] (estatística da imagem)
- lpar nomedotask (lista parâmetros)
- cl < nomedoscript.cl (roda script)

ccdproc
- zerocombine (combina os bias)
- flatcombine (combina os flats)
- darkcombine (combina os darks)
- cccproc (faz a preparação das imagens de calibração, bem como reduz as imagens de ciência)


## Observatório Astronômico do Sertão de Itaparica (OASI)

The specifications like read-noise and gain for the telescope that were used are following

- rdnoise = 9 e-
- gain = 1.175

