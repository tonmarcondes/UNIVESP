package teste.src;
public class arquivo2{
    public static void main(String[] args) {
        arquivo1 ton1 = new arquivo1();
        ton1.altura = 168;
        ton1.cor = "Preta";
        ton1.idade = 42;
        ton1.numSapato = 40;
        ton1.olhosClaros = true;
        ton1.temPernas = false;
        ton1.status();  
        ton1.olhar();
        ton1.emPe();
        ton1.correr();
    }
}