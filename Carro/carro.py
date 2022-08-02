class carro: #aqui se crea el carrito de compras
    def __init__(self, request):
        self.request==request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        else:
            self.carro= carro
            
    def agregar(self, producto): #funcion para agregar un producto
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen":producto.imagen.url,
            }
            
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
                    
        self.guardar_carro()            
        
    
    def guardar_carro(self): #funcion poara guardar el carrito de comprar
        self.session["carro"]=self.carro
        self.session.modified=True
        
    def eliminar(self, producto):
        producto.id= str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
            
    def restar_producto(self,producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    break
        self.guardar_carro()
                    
        
            
        
        
