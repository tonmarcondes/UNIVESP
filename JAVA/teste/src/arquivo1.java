package teste.src;
public class arquivo1 {
    String cor;
    int altura;
    int idade;
    int numSapato;
    boolean olhosClaros;
    boolean temPernas;
    void status(){
        System.out.println("\nA cor do Ton é: " + this.cor);
        System.out.println("sua altura em cm é: " + this.altura);
        System.out.println("com uma idade de: " + this.idade + " anos");
        System.out.println("Calça sapatos nº: " + this.numSapato);
        System.out.println("Tem olhos claros? " + this.olhosClaros);
        System.out.println("Tem pernas? " + this.temPernas + "\n");

    }

    void emPe(){
        if (!this.temPernas){
            System.out.println("Ta doido, não tenho pernas");
        } else {
            System.out.println("Estou em pé");
        }
    }
    void correr(){
        if(this.temPernas){
            System.out.println("Voa menino, as pernas foram feitas pra correr");
        } else {
            System.out.println("Muito feio de sua parte fazer bulling com quem não tem nem mesmo como andar :(\n");
        }
    }
    void olhar(){
        if (this.olhosClaros){
            System.out.println("Olhar 43 com meus olhos claros");
        } else {
            System.out.println("Olhar de olhos de jabuticaba");
        }
    }
}
