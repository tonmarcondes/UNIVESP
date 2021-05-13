package pacote.src;
public class mensagem {
    public static void main(String[] args) {
        mensagemCelula msg = new mensagemCelula();
        msg.tema = "O fim está próximo";
        msg.dataEntrega = "13/05/2021";
        msg.maioriaJovem = true;
        msg.qtdPerguntas = 3;
        msg.rede = "Conectados";
        msg.msgPronta = false;
        msg.status();
        msg.estudar();
    }

}
