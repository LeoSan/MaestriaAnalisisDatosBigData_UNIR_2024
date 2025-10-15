
# Vector 
# Notas 
# Los vectores son de un mismo tipo
vector_1 <-c(1,2,3,4,5)
vector 


vector_2 <-c("hola", "soy", "Vector", "Caracteres")
vector_2

## Valores secuencial 

a<- 1:10
a 


## Valores repetidos 
b<-rep(5, times=10)
b


## Valor metodo rep con c de concatenar 
c <-rep(c(1,2), times=4)
c 

## Metodo each 

d<-rep(c(1,2), each = 3)
d

e<-rep(c(1,2), times = 2, each = 3)
e

## Controlar la salida con el elemento length.out = 8
f<-rep(1:3, length.out = 8)
f


## acceder por posiciones 
g<-c("a", "b", "c")
g[0:2]


## Metodo de Secuencia seq(from, to, by, length.out)

seq(1,10,2)



## acceder por posiciones 
h<-c("a", "b", "c", "d", "f")
h[seq(1,4, by=2)]

## Graficos integrados 
x<-seq(0,2*pi, length.out =100)
y<-sin(x)

#plot(x,y,type="1")


## Puedes usar logica dentro de los corchetes del vector
v<-c(10,20,30,40,50,60,70)
v[v>25]
v[v %% 20==0 ]

v[2]<-99
v

## mean la media aritmetica, sd => desviacion standart
mean(v)
sd(v)
sort(v)
summary(v)


## Como usar Matrix se usa la palabra matrix(data, nrow, ncol, byrow=FALSE)

m<-matrix(1:6, nrow=2, ncol=3)
m

n<-matrix(1:8, nrow=2, ncol=3, byrow=FALSE)
n

## Como accedemos 

n[1,3] = 99
n

## Validr dimenciones usamos el metodo dim()
dim(n)
ncol(n)
nrow(n)

## Tambien podemos ejecutar operaciones entre matrices 
m +n
m -n
m *n