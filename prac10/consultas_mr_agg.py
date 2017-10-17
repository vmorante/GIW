# -*- coding: utf-8 -*-
"""
Autores: XXX
Grupo YYY

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""


# Importaciones
from bottle import get, run
from pymongo import MongoClient
from bson.code import Code
from bson.son import SON

# MapReduce: usuarios en cada pais.
@get('/users_by_country_mr')
def users_by_country_mr():
   mongoClient = MongoClient('localhost',27017)
   db = mongoClient.giw
   
   collection = db.users
   
   mapper = Code("""
               function () {
                   z = this.country;
                   emit(z, 1);
               }
               """)
               
   reducer = Code("""
               function (key, values) {
                   var total = 0;
                   for (var i = 0; i < values.length; i++) {
                       total += values[i];
                   }
                   return total;
                }
                """)
                
   results = collection.inline_map_reduce(mapper, reducer)
   
   for result in results:
       print result

   
   
   
# Aggregation Pipeline: usuarios en cada pais (orden descendente por numero
# de usuarios).
@get('/users_by_country_agg')
def users_by_country_agg():
   mongoClient = MongoClient('localhost',27017)
   db = mongoClient.giw
   
   collection = db.users
   
   pipeline = [
       {"$group": {"_id": "$country", "Num_usuarios": {"$sum": 1}}},
       {"$sort": {"Num_usuarios", -1}}
       ]
       
   results = list(collection.aggregate(pipeline))
   
   for result in results:
       print result
    
    
# MapReduce: gasto total en cada pais.
@get('/spending_by_country_mr')
def spending_by_country_mr():
   mongoClient = MongoClient('localhost',27017)
   db = mongoClient.giw
   
   collection = db.users
   
   mapper = Code("""
               function () {
                   z = this.country;
                   values = this.orders;
                   n = values.length();
                   var total = 0;
                   for (var i = 0; i < n; i++){
                       total += values[i].total;
                   }
                   emit(z, total);
               }
               """)
               
   reducer = Code("""
               function (key, values) {
                   var total = 0;
                   for (var i = 0; i < values.length; i++) {
                       total += values[i];
                   }
                   return total;
                }
                """)
                
   results = collection.inline_map_reduce(mapper, reducer)
   
   for result in results:
       print result


# Aggregation Pipeline: gasto total en cada pais (orden descendente por nombre
# del pais).
@get('/spending_by_country_agg')
def spending_by_country_agg():
   mongoClient = MongoClient('localhost',27017)
   db = mongoClient.giw
   
   collection = db.users
  
   pipeline = [
       {"$unwind": "$orders"},
       {"$group": {"_id": "$country", "Total gastos": {"$sum": "$orders.total"}}}
       ]
       
   results = list(collection.aggregate(pipeline))
   
   for result in results:
       print result
       


# MapReduce: gasto total realizado por las mujeres que han realizdo EXACTAMENTE
# 3 compras.
@get('/spending_female_3_orders_mr')
def spending_female_3_orders_mr():
   mongoClient = MongoClient('localhost',27017)
   db = mongoClient.giw
   
   collection = db.users
   
   mapper = Code("""
               function () {
                   if this.gender == "Female" && this.orders.lenght == 3{
                       z = this.gender;
                       var total = 0;
                       for (var i = 0, i<this.orders.lenght; i++){
                           total += this.orders[i].total;
                           }
                       emit(z, 1);
                   }else{
                       emit("Female",0);
                   }
                   
               }
               """)
               
   reducer = Code("""
               function (key, values) {
                   var total = 0;
                   for (var i = 0; i < values.length; i++) {
                       total += values[i];
                   }
                   return total;
                }
                """)
                
   results = collection.inline_map_reduce(mapper, reducer)
   
   for result in results:
       print result


# Aggregation Pipeline: gasto total realizado por las mujeres que han realizdo 
# EXACTAMENTE 3 compras.
@get('/spending_female_3_orders_agg')
def spending_female_3_orders_agg():
   mongoClient = MongoClient('localhost',27017)
   db = mongoClient.giw
   
   collection = db.users
   
   pipeline = [
       {"$match": {"Gender": "Female"}, "Orders.length()": {'$gte': 3}},
       {"$unwind": "$orders"},
       {"$group": {"$_id": "$Gender", "Gasto total" : {"$sum": "orders.total"}}}
       ]
       
   results = list(collection.aggregate(pipeline))
   
   for result in results:
       print result
    
    
###############################################################################
###############################################################################

if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)





