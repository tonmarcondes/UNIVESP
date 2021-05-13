package pacote.src;
public class mensagemCelula {
    String tema;
    int qtdPerguntas;
    String rede;
    String dataEntrega;
    boolean maioriaJovem;
    boolean msgPronta;

    void status(){
        System.out.println("\nO tema da mensagem é: " + this.tema);
        System.out.println("Total de perguntas: " + this.qtdPerguntas);
        System.out.println("Rede: " + this.rede);
        System.out.println("A data de entrega da mensagem será dia " + this.dataEntrega);
        System.out.println("Pode se dizer que a rede " + this.rede + "possui uma característica majoritariamente jovem? " + this.maioriaJovem);
        System.out.println("A mensagem já está pronta? " + this.msgPronta);
    }
    void estudar(){
        System.out.println("\nPreparando a mensagem " + this.tema);    
    }
}
