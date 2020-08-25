# -*- coding: utf-8 -*-

from os import path
from analisador_de_imagem import AnalisadorDeImagem
import imghdr



print('\t\tBem vindo ao MCCCircleCounter')
print('\t\t==============================')
#captura quantidade de imagens que se deseja analisar
numeroValido = False

while not numeroValido:
    try:
        qtd_imgs = int(input('Digite a quantidade de imagens que deseja adicionar, ou um valor menor ou igual a zero, para sair:'))
        numeroValido=True
    except Exception:
        print('opção inválida, tente novamente')

if qtd_imgs > 0:
    i = 0
    while(i < qtd_imgs):
        try:
            path_image = input('Digite o caminho da {}ª imagem que deseja analisar: '.format(i+1))
            #verifica se path existe e se eh uma imagem comercial
            if path.exists(path_image) and not imghdr.what(path_image) is None: 
                i = i+1
                analisador = AnalisadorDeImagem(path_image)
                circulos_detectados = analisador.localizaCirculos()
                qtdCircuculos = analisador.informacoesSobreCirculos(circulos_detectados)
                print('{} círculos forma identificados!'.format(qtdCircuculos))
                
                #verifica se ha circulos para exibir
                if qtdCircuculos > 0:
                    opcao_valida = False
                    while not opcao_valida:
                        imprimir_imagem = input('Você deseja exibir imagem com círculos detectados? (SIM/nao): ')
                        
                        if len(imprimir_imagem) == 0 or imprimir_imagem.lower() == 'sim':
                            analisador.imprimeImagem(analisador.desenhaCirculosNaImagem(circulos_detectados))
                            opcao_valida = True
                        elif imprimir_imagem.lower() == 'nao':
                            opcao_valida = True
                        else:
                            print('opção inválida tente novamente')
            else:
                print('Arquivo não existe ou não é uma imagem válida. Por favor digite um caminho válido')
        except Exception as e:
            ('erro desconhecido, tente novamente, mensagem: {}'.format(str(e)))
        
    