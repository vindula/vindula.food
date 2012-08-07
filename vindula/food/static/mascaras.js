			
			
		$j = jQuery.noConflict();
		$j(document).ready(function(){
		/* Aba de edição do conteudo*/
		$j('#contentview-restaurant').addClass('selected');
		$j('#contentview-view').removeClass('selected');
		})
				
    
	    /*Função telefone*/
	 function Mascara(objeto){
	 	 if(objeto.value.length == 0)
			objeto.value = '(' + objeto.value;	
			if(objeto.value.length == 3)
			     objeto.value = objeto.value + ')';
				 if(objeto.value.length == 8)
				     objeto.value = objeto.value + '-';
				}
			
			
	/* Função que padroniza as datas e/ou horas inseridas 14:30 ou 12/12/2012*/
		function mascara(m, o) {
			        o.onkeyup = function(e) {
			                if(e.keyCode != 8) {
			                        var array_m = m.split('')
			                        var array_o_value = o.value.split('')
			                        retorno = new Array()
			                        for(var i=0; array_o_value[i]; i++) {
			                                retorno[i] = array_m[i] == '#' ? array_o_value[i] : array_m[i]
			                                if(i == array_o_value.length - 1 && array_m[i+1] && array_m[i+1] != '#') retorno[i+1] = array_m[i+1]
			                        }
			                        
			                        o.value = retorno.join('')
			                }
			        }
			}