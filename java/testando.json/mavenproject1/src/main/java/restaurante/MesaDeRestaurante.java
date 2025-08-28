/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package restaurante;
import java.util.Scanner;
//import java.util.List;
import java.util.ArrayList;
/**
 *
 * @author cassio
 */
public class MesaDeRestaurante {
    ArrayList pedidosLinha = new ArrayList<String>();
    //ArrayList pedidosColuna = new ArrayList<>();
    
    //pedidos[indice][pedido]    
    public void adicionaAoPedido(){
        int controleDePedido = 0;
        //pedidosLinha.add(new ArrayList<>());
        //pedidos.add(new ArrayList<>());
        //inicializando lista de array

        Scanner ler = new Scanner(System.in);
        String novoPedido = ler.nextLine();
        //lendo pedido a ser adicionado
        pedidosLinha.add(controleDePedido,novoPedido);
        
        controleDePedido++;
        
    }
    public void zeraPedidos(){
        pedidosLinha.clear();
    }
    public void calculaTotal(){
        System.out.println(pedidosLinha);
    }
    
}
