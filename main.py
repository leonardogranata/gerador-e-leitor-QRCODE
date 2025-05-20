import qrcode
from PIL import Image
from pyzbar.pyzbar import decode


def codificador():
    mensagem = str(input("Digite a mensagem/link a transformar em qrcode: "))

    qr = qrcode.QRCode(version=1, box_size=10, border=5) # Faz o qrcode com suas configurações

    # Adiciona a mensagem digitada ao QR Code
    qr.add_data(mensagem)

    # Constrói o QR Code com ajuste automático de tamanho se necessário
    qr.make(fit=True)

    # Gera uma imagem do QR Code com cores personalizadas
    img = qr.make_image(fill_color='black', back_color='white')

    img.save('C:/Users/ADM/Desktop/meu_qrcode.png') # Salva no caminho da pasta

def decodifacor():
    img = Image.open('C:/Users/ADM/Desktop/meu_qrcode.png')   # No caminho específico
    resultado = decode(img)

    print(resultado)


while True:
    print("O que você deseja fazer?")
    print("[1] - Codificar mensagem em qrcode\n[2] - Decodificar mensagem em qrcode\n[3] - Sair")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        codificador()
    elif opcao == 2:
        decodifacor()
    elif opcao == 3:
        break
    else:
        print("Opção inválida")
        continue
