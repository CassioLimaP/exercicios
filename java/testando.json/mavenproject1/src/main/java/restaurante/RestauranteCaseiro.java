/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package restaurante;

/**
 *
 * @author cassio
 */
public class RestauranteCaseiro {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        System.out.println("adicionando ao pedido");
        MesaDeRestaurante mesa1 = new MesaDeRestaurante();
        mesa1.adicionaAoPedido();
        mesa1.calculaTotal();
    }
    
}