import java.util.*; 
import java.lang.*; 
import java.io.*; 
class MST { 
 // nro de vertices
 int V = 4; 

//nos retorna el indice del nodo, con el peso minimo
 public int minIndice(int nodos[], Boolean visitado[]) { 
     // Initialize min value 
     int min = Integer.MAX_VALUE, min_index = -1; 

     for (int v = 0; v < V; v++) {
    	 // si el vertice "v" no esta visitado
    	 // y el peso del nodo[v] es menor al peso inicial,
    	 // que es infinito
    	 //y asi sucesivaemnte hasta encontrar el indice del nodo
    	 //con el menor peso
    	 if (visitado[v] == false && nodos[v] < min) {  
             min = nodos[v]; 
             min_index = v; 
         }
     }
          
     //nos retorna el min_index
     return min_index; 
 } 

 //nos devuelve el peso minimo del MST
 public int pesoMin(int padres[], int grafo[][]) { 
     int s = 0;
     for (int i = 1; i < V; i++) 
         s+=grafo[i][padres[i]];
     return s;
 } 

 //este es el encargado de construir el minimum spanning tree(MST)
 void MST(int grafo[][]) { 
     // este guardara los nodos padre del indice respectivo
	 // si el indice es v, entonces padres[v] = u
	 //entonces el padre de v, es u
     int padres[] = new int[V]; 
 
     int nodos[] = new int[V]; 

     // representa a los nodos ya visitados de acuerdo al indice
     Boolean visitado[] = new Boolean[V]; 

     // incializa todos los nodos en pesos de Infinito
     // y marcarlos en false todos
     for (int i = 0; i < V; i++) { 
         nodos[i] = Integer.MAX_VALUE; 
         visitado[i] = false; 
     } 

     //este sera el vertice "0" con el que se inicia el MST 
     nodos[0] = 0;
     // ahora recorremos todos los vertices
     for (int k = 0; k < V - 1; k++) { 
         //primero agarramos los el vertice con el minimo peso hacia el vertice 
    	 // de inicio
         int u = minIndice(nodos, visitado); 

         //lo ponemos como visitado
         visitado[u] = true; 

         //ahora recorremos los indices adyacentes al indice "u"
         for (int v = 0; v < V; v++) 
             //  Ahora los evaluamos
        	 // si es cero la arista, significa que es cero, osea no cuenta
        	 // si el vertice adyacente "v" es falso, signifia que aun no se ha visitado
        	 // luego si cumple todas estas condiciones, vemos esas aristas adyacentes
        	 // que cumplen las condiciones anteriores, entonces ...
             if (grafo[u][v] != 0 && visitado[v] == false && grafo[u][v] < nodos[v]) {
            	 // hacemos que el padre de v, sea u
                 padres[v] = u; 
                 //luego asignamos, a la que hasta ahora es la arista minima
                 nodos[v] = grafo[u][v]; 
             } 
     } 
     // luego retornamos el peso minimo
       
     int p = pesoMin(padres, grafo);
     System.out.println(p);
    
 } 

 public static void main(String[] args) 
 { 
     MST t = new MST(); 
     int grafo[][] = new int[][] { { 0 ,6 , 5, 0 }, 
                                   { 6 ,0, 1,2 }, 
                                   { 5 ,1 ,0 ,10 }, 
                                   { 0 ,2 ,10 ,0 }, 
                                   }; 
      // las relaciones entre ciudades
     /*		  LISBON LONDON PARIS BERLIN  
      LISBON   0        6      5     0                        
      LONDON   6        0      1     2            
      PARIS    5        1      0     10           
      BERLIN   0        2     10     0               
      */                              
     //retornamos el peso minimo
     t.MST(grafo); 
 } 
} 