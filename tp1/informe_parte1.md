
## Parte 1: Cálculo empírico de tiempos de ejecución

### Consigna

Implementar los siguientes algoritmos de ordenamiento para números enteros positivos:

* Selección
* Inserción
* Quicksort
* Heapsort
* Mergesort

a) Para cada uno de ellos analizar su complejidad teórica y compararlos (tiempo promedio y peor tiempo). Tener en cuenta las constantes para la comparación.

b) Construir 10 sets de números aleatorios con 10.000 números positivos.

c) Calcular los tiempos de ejecución de cada algoritmo utilizando los primeros: 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000 números de cada set.

d) Estimar los tiempos medios de ejecución para cada rango-algoritmo y graficar.

e) Determinar para cada algoritmo anterior las características que debe tener un set para que se comporte de la peor forma posible (si el algoritmo lo permite).

f) Construir para cada algoritmo y para los rangos del punto “C” sets con las peores características y evaluar los tiempos de ejecución. Comparar con los generados con los sets aleatorios y graficar.

g) En base a los tiempos obtenidos compare con los valores teóricos y analice (Extensión máxima de 2 párrafos).

### Solución
a)

| Algoritmo | Complejidad teórica( Promedio ) | Mejor caso  | Peor caso |
| ----------|---------------------------------| ------------| -------- |
| Selección | *$\Theta(n^2)$*        | *$\Theta(n^2)$* | *$\Theta(n^2)$* |
| Inserción | *$\Theta(n^2)$*       |*$\Theta(n)$*| *$\Theta(n^2)$*|
| Quicksort | *$\Theta(n \log n)$*   | *$\Theta(n)$* | *$\Theta(n^2)$* |
| Heapsort  | *$\Theta(n \log n)$*  |*$\Theta(n)$*|*$\Theta(n \log n)$*|
| Mergesort | *$\Theta(n \log n)$*  |*$\Theta(n)$*|*$\Theta(n \log n)$*|

c) Tiempos de ejecución
#### Set0
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.00036444700072024716 |
| Selección | 0.00014536199978465447 |
| MergeSort | 0.00038026299989724066 |
| Quicksort | 0.00022003699996275827 |
| Inserción | 0.00020109799970668973 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0013417600002867403 |
| Selección | 0.0008998510002129478 |
| MergeSort | 0.0009564530000716331 |
| Quicksort | 0.00027484500060381833 |
| Inserción | 0.0004023749997941195 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.005462087999148935 |
| Selección | 0.012406216000272252 |
| MergeSort | 0.0033275269997830037 |
| Quicksort | 0.001671993999480037 |
| Inserción | 0.01129564299935737 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.011647569999695406 |
| Selección | 0.04873682800007373 |
| MergeSort | 0.00616464500035363 |
| Quicksort | 0.003511734999847249 |
| Inserción | 0.04151257500052452 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.023934383000778325 |
| Selección | 0.1820100340000863 |
| MergeSort | 0.0123739350001415 |
| Quicksort | 0.007363482000073418 |
| Inserción | 0.16876025900000968 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.03783640199981164 |
| Selección | 0.40705413999967277 |
| MergeSort | 0.018953632000375364 |
| Quicksort | 0.013176619999285322 |
| Inserción | 0.3857335700004114 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.05206082200038509 |
| Selección | 0.7262599499999851 |
| MergeSort | 0.025829143000009935 |
| Quicksort | 0.015532585000073595 |
| Inserción | 0.6815220509997744 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0707400740002413 |
| Selección | 1.17423241600045 |
| MergeSort | 0.03318820799995592 |
| Quicksort | 0.019164805999935197 |
| Inserción | 1.0421252050000476 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10557932299980166 |
| Selección | 2.5338925790001667 |
| MergeSort | 0.05047495000053459 |
| Quicksort | 0.03153415899942047 |
| Inserción | 2.3582192169997143 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.14534850699965318 |
| Selección | 4.4873209620000125 |
| MergeSort | 0.06867896799940354 |
| Quicksort | 0.043427092999991146 |
| Inserción | 4.218447881999964 |
#### Set1
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.00032754499989096075 |
| Selección | 0.00013121900065016234 |
| MergeSort | 0.0002362609993724618 |
| Quicksort | 0.00012027800039504655 |
| Inserción | 0.00010869600009755231 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.000731492999875627 |
| Selección | 0.00044715300009556813 |
| MergeSort | 0.0004763690003528609 |
| Quicksort | 0.00022806800006947014 |
| Inserción | 0.00040316200011147885 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.004940451000038593 |
| Selección | 0.011084334000770468 |
| MergeSort | 0.00274071800049569 |
| Quicksort | 0.0017564809995747055 |
| Inserción | 0.009349189999738883 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.01097157200001675 |
| Selección | 0.04561488699982874 |
| MergeSort | 0.005859105999661551 |
| Quicksort | 0.0032516589999431744 |
| Inserción | 0.0409107719997337 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.023867126000368444 |
| Selección | 0.18091704400012532 |
| MergeSort | 0.01236154100024578 |
| Quicksort | 0.007404164000035962 |
| Inserción | 0.16327079000075173 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.037797219000822224 |
| Selección | 0.4075815659998625 |
| MergeSort | 0.018988193999575742 |
| Quicksort | 0.011843107000458986 |
| Inserción | 0.37150006699994265 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.05197898999995232 |
| Selección | 0.7271466600004715 |
| MergeSort | 0.02586022299965407 |
| Quicksort | 0.015511165999669174 |
| Inserción | 0.6605659710003238 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06690154700027051 |
| Selección | 1.1268436629998178 |
| MergeSort | 0.0328367279998929 |
| Quicksort | 0.02156521199958661 |
| Inserción | 1.0415184129997215 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10515600600047037 |
| Selección | 2.555618580000555 |
| MergeSort | 0.05133223299981182 |
| Quicksort | 0.030933952000850695 |
| Inserción | 2.363872528000684 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.1449736849999681 |
| Selección | 4.527198487000533 |
| MergeSort | 0.06866317999993043 |
| Quicksort | 0.042514855000263196 |
| Inserción | 4.2402962899996055 |
#### Set2
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.000329194999721949 |
| Selección | 0.00013106699952913914 |
| MergeSort | 0.0002552519999881042 |
| Quicksort | 0.00012414000048011076 |
| Inserción | 8.66250002218294e-05 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0007275829993886873 |
| Selección | 0.00044829199941887055 |
| MergeSort | 0.000478320000183885 |
| Quicksort | 0.00024553700040996773 |
| Inserción | 0.00042129399935220135 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.00483928400080913 |
| Selección | 0.011094995000348717 |
| MergeSort | 0.0027368069995645783 |
| Quicksort | 0.0013791219998893212 |
| Inserción | 0.009936387999914587 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.010800451999784855 |
| Selección | 0.04526351899949077 |
| MergeSort | 0.005848566999702598 |
| Quicksort | 0.0034092340001734556 |
| Inserción | 0.04091285499998776 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.023804240999197646 |
| Selección | 0.1814312679998693 |
| MergeSort | 0.01227286900029867 |
| Quicksort | 0.00776275699990947 |
| Inserción | 0.1673246910004309 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.03881058400020265 |
| Selección | 0.411555104999934 |
| MergeSort | 0.018940904000373848 |
| Quicksort | 0.012224507000610174 |
| Inserción | 0.3829390479995709 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0534501279998949 |
| Selección | 0.7288111870002467 |
| MergeSort | 0.02574289200038038 |
| Quicksort | 0.015436638000210223 |
| Inserción | 0.6781714729995656 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06699421699977393 |
| Selección | 1.1328520460001528 |
| MergeSort | 0.03269966399966506 |
| Quicksort | 0.02169279000008828 |
| Inserción | 1.0502489539994713 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10528664199955529 |
| Selección | 2.5372855400000844 |
| MergeSort | 0.05047760799971002 |
| Quicksort | 0.03244621600060782 |
| Inserción | 2.3583186890000434 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.14475488599964592 |
| Selección | 4.524359852000089 |
| MergeSort | 0.06870937699932256 |
| Quicksort | 0.04563804000008531 |
| Inserción | 4.200854101999539 |
#### Set3
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0003221440001652809 |
| Selección | 0.000130890000036743 |
| MergeSort | 0.0002448389996061451 |
| Quicksort | 0.00011960200026805978 |
| Inserción | 0.00011742000060621649 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.000741881999601901 |
| Selección | 0.00045452199992723763 |
| MergeSort | 0.0004977150001650443 |
| Quicksort | 0.00024417399981757626 |
| Inserción | 0.00038653599949611817 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.004878287000792625 |
| Selección | 0.011062261000006401 |
| MergeSort | 0.002745001999755914 |
| Quicksort | 0.0014061439997021807 |
| Inserción | 0.009487399000136065 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.010884323000027507 |
| Selección | 0.0454017339998245 |
| MergeSort | 0.006014221999976144 |
| Quicksort | 0.0030797839999650023 |
| Inserción | 0.04160808899996482 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.023867072999564698 |
| Selección | 0.1812193780006055 |
| MergeSort | 0.012271869999494811 |
| Quicksort | 0.007468185999641719 |
| Inserción | 0.1672441129994695 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.03784568300034152 |
| Selección | 0.4070661759997165 |
| MergeSort | 0.018971482999404543 |
| Quicksort | 0.011945727000238548 |
| Inserción | 0.37603049500012276 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.05206895199989958 |
| Selección | 0.7334110460005832 |
| MergeSort | 0.026701420000790677 |
| Quicksort | 0.018893180999839387 |
| Inserción | 0.677279389999967 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06694465300006414 |
| Selección | 1.1301502369997252 |
| MergeSort | 0.033837717000096745 |
| Quicksort | 0.022226541999771143 |
| Inserción | 1.05431986900021 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10501477100024204 |
| Selección | 2.5287869639996643 |
| MergeSort | 0.050545512000098825 |
| Quicksort | 0.03288862200042786 |
| Inserción | 2.371686497000155 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.1448125880006046 |
| Selección | 4.493042980999235 |
| MergeSort | 0.06867694799984747 |
| Quicksort | 0.04136468800061266 |
| Inserción | 4.171316103999743 |
#### Set4
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.00033248300042032497 |
| Selección | 0.00013248799950815737 |
| MergeSort | 0.0002349420001337421 |
| Quicksort | 0.0001323040005445364 |
| Inserción | 0.00010032899990619626 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0007346330003201729 |
| Selección | 0.0004472600003282423 |
| MergeSort | 0.00047826500031078467 |
| Quicksort | 0.0002464360004523769 |
| Inserción | 0.0003717950003192527 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0048925730006885715 |
| Selección | 0.011017503999937617 |
| MergeSort | 0.0027464069999041385 |
| Quicksort | 0.0015425390001837513 |
| Inserción | 0.009703667999929166 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.010852997999791114 |
| Selección | 0.04492592299993703 |
| MergeSort | 0.005817448000016157 |
| Quicksort | 0.003333296999699087 |
| Inserción | 0.04060472600031062 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.02384392700059834 |
| Selección | 0.17935056300029828 |
| MergeSort | 0.012270131000150286 |
| Quicksort | 0.007054458999846247 |
| Inserción | 0.16670681400046305 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.03771272599988151 |
| Selección | 0.4058258589993784 |
| MergeSort | 0.01896500700058823 |
| Quicksort | 0.012236962000315543 |
| Inserción | 0.37636649900014163 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.052265655000155675 |
| Selección | 0.7156834409997828 |
| MergeSort | 0.025868445000014617 |
| Quicksort | 0.015507280999372597 |
| Inserción | 0.6661003700000947 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06697418300063873 |
| Selección | 1.12350440299997 |
| MergeSort | 0.03278017100001307 |
| Quicksort | 0.02157677099967259 |
| Inserción | 1.058976070999961 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10530624399962107 |
| Selección | 2.5289850100007243 |
| MergeSort | 0.050380708999909984 |
| Quicksort | 0.03126227799930348 |
| Inserción | 2.369602421000309 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.14563854100015305 |
| Selección | 4.491545454000516 |
| MergeSort | 0.0708093879993612 |
| Quicksort | 0.044001987999763514 |
| Inserción | 4.245434956999816 |
#### Set5
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0003371290003997274 |
| Selección | 0.00013413499982561916 |
| MergeSort | 0.00024262800070573576 |
| Quicksort | 0.0001283190003960044 |
| Inserción | 0.00010365699927206151 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.000758039999709581 |
| Selección | 0.00046172500060492894 |
| MergeSort | 0.0004923469996356289 |
| Quicksort | 0.0002773610003714566 |
| Inserción | 0.00039133999962359667 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.00509236800007784 |
| Selección | 0.011427886999626935 |
| MergeSort | 0.00285742400046729 |
| Quicksort | 0.0015433990001838538 |
| Inserción | 0.009874327999568777 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.011176283999702719 |
| Selección | 0.046799552000265976 |
| MergeSort | 0.006010648000483343 |
| Quicksort | 0.003490787999908207 |
| Inserción | 0.04307526600041456 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.024590836000243144 |
| Selección | 0.18138315200030775 |
| MergeSort | 0.012353334999716026 |
| Quicksort | 0.007815683000444551 |
| Inserción | 0.16986986299980344 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.03762192999965919 |
| Selección | 0.4059855460000108 |
| MergeSort | 0.01890024899967102 |
| Quicksort | 0.011522977999447903 |
| Inserción | 0.3900910889997249 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.05196882000018377 |
| Selección | 0.7208056619992931 |
| MergeSort | 0.025800023000556394 |
| Quicksort | 0.015789635000146518 |
| Inserción | 0.6791269360001024 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06751116500072385 |
| Selección | 1.1353559339995627 |
| MergeSort | 0.03312687900051969 |
| Quicksort | 0.02074365999942529 |
| Inserción | 1.077598061999197 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10526940499948978 |
| Selección | 2.54155035399981 |
| MergeSort | 0.05037642200022674 |
| Quicksort | 0.032485380999787594 |
| Inserción | 2.368908935000036 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.14514236099967093 |
| Selección | 4.5450299089998225 |
| MergeSort | 0.06977804899997864 |
| Quicksort | 0.045546151000053214 |
| Inserción | 4.230106899999555 |
#### Set6
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0003274310001870617 |
| Selección | 0.00013226800001575612 |
| MergeSort | 0.00023645199962629704 |
| Quicksort | 0.0001203480005642632 |
| Inserción | 0.00010785400081658736 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0007624350000696722 |
| Selección | 0.00044797600003221305 |
| MergeSort | 0.00047765700037416536 |
| Quicksort | 0.00021830200057593174 |
| Inserción | 0.0004035849997308105 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0048393520000900025 |
| Selección | 0.011149078000016743 |
| MergeSort | 0.002742042999670957 |
| Quicksort | 0.0014468980007222854 |
| Inserción | 0.009829523999542289 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.011035782999897492 |
| Selección | 0.04540791699946567 |
| MergeSort | 0.0058592240002326434 |
| Quicksort | 0.0034426939992044936 |
| Inserción | 0.040579647999948065 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.02379733399993711 |
| Selección | 0.1810823280002296 |
| MergeSort | 0.012309708999964641 |
| Quicksort | 0.00801576899993961 |
| Inserción | 0.1612820219997957 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.037774101999275445 |
| Selección | 0.4066470979996666 |
| MergeSort | 0.01901943599932565 |
| Quicksort | 0.01230176199987909 |
| Inserción | 0.37673979999999574 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.05362828899978922 |
| Selección | 0.7248161240004265 |
| MergeSort | 0.026223028999993403 |
| Quicksort | 0.016272255000330915 |
| Inserción | 0.6746021909993942 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06693085900042206 |
| Selección | 1.1306068649992085 |
| MergeSort | 0.03273063500000717 |
| Quicksort | 0.020610373000636173 |
| Inserción | 1.0577177969998957 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10532910100027948 |
| Selección | 2.534811945999536 |
| MergeSort | 0.050732904999676975 |
| Quicksort | 0.03240823700070905 |
| Inserción | 2.3817839720004486 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.14573271100016427 |
| Selección | 4.527330685000379 |
| MergeSort | 0.06956791900029202 |
| Quicksort | 0.048866866000025766 |
| Inserción | 4.221061616000043 |
#### Set7
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.00032341399946744787 |
| Selección | 0.00013040200065006502 |
| MergeSort | 0.00023546299962617923 |
| Quicksort | 0.00011077100043621613 |
| Inserción | 0.00010812999971676618 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0007230519995573559 |
| Selección | 0.0004464069997993647 |
| MergeSort | 0.0004802780003956286 |
| Quicksort | 0.00024240499988081865 |
| Inserción | 0.0004050600000482518 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0048517650002395385 |
| Selección | 0.011132573999930173 |
| MergeSort | 0.002761319000455842 |
| Quicksort | 0.0014551129997926182 |
| Inserción | 0.010017736000008881 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.010800195000228996 |
| Selección | 0.04519991600045614 |
| MergeSort | 0.0058496800002103555 |
| Quicksort | 0.003493509999316302 |
| Inserción | 0.040290543000082835 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.024033710999901814 |
| Selección | 0.18172708099973534 |
| MergeSort | 0.012365363999379042 |
| Quicksort | 0.0076344449998941855 |
| Inserción | 0.16901372599932074 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.03768476000004739 |
| Selección | 0.4109108909997303 |
| MergeSort | 0.018952533000629046 |
| Quicksort | 0.012357857000097283 |
| Inserción | 0.3813641729993833 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.05212698099967383 |
| Selección | 0.7245644459999312 |
| MergeSort | 0.025854866999907244 |
| Quicksort | 0.015465718000086781 |
| Inserción | 0.6799944439999308 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06757961800030898 |
| Selección | 1.1299024949994418 |
| MergeSort | 0.03280165999967721 |
| Quicksort | 0.020631728000807925 |
| Inserción | 1.0629488009999477 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10679128099945956 |
| Selección | 2.5356280089999927 |
| MergeSort | 0.050641920999623835 |
| Quicksort | 0.033704125999975076 |
| Inserción | 2.356627741999546 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.14477702200019849 |
| Selección | 4.489329130000442 |
| MergeSort | 0.06843693900009384 |
| Quicksort | 0.04440720899947337 |
| Inserción | 4.232616121000319 |
#### Set8
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.00032850500065251254 |
| Selección | 0.00013023700012126938 |
| MergeSort | 0.00023618700015504146 |
| Quicksort | 0.00014231799923436483 |
| Inserción | 9.866199980024248e-05 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0007190289998106891 |
| Selección | 0.0004478760001802584 |
| MergeSort | 0.0004773680002472247 |
| Quicksort | 0.00026477099982002983 |
| Inserción | 0.00038916799985599937 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.004849613000260433 |
| Selección | 0.011041255999771238 |
| MergeSort | 0.0027362479995645117 |
| Quicksort | 0.0014626439997300622 |
| Inserción | 0.010607070999867574 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.010813965000124881 |
| Selección | 0.04489263100003882 |
| MergeSort | 0.005825520000144024 |
| Quicksort | 0.003382656999747269 |
| Inserción | 0.0412133959998755 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.023860536000029242 |
| Selección | 0.17915704700044444 |
| MergeSort | 0.012267421000615286 |
| Quicksort | 0.007436365999637928 |
| Inserción | 0.16672240300067642 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.03765693199966336 |
| Selección | 0.40631579699947906 |
| MergeSort | 0.019010790999345772 |
| Quicksort | 0.011299943999802053 |
| Inserción | 0.3768302460002815 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0520846569997957 |
| Selección | 0.7199754909997864 |
| MergeSort | 0.02646642400031851 |
| Quicksort | 0.01550951100034581 |
| Inserción | 0.6649729520004257 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06731055499949434 |
| Selección | 1.120895809999638 |
| MergeSort | 0.032792344999506895 |
| Quicksort | 0.022717073999956483 |
| Inserción | 1.0466918660004012 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10589120799977536 |
| Selección | 2.5301297280002473 |
| MergeSort | 0.05034855400026572 |
| Quicksort | 0.033414731999982905 |
| Inserción | 2.398666993000006 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.14751086800060875 |
| Selección | 4.503560135000043 |
| MergeSort | 0.07085552199987433 |
| Quicksort | 0.04566599400004634 |
| Inserción | 4.2364737380003135 |
#### Set9
**Cantidad de elementos: 50**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0003317970003990922 |
| Selección | 0.00013075100014248164 |
| MergeSort | 0.0002343539999856148 |
| Quicksort | 0.00011366400030965451 |
| Inserción | 9.817899990594015e-05 |
**Cantidad de elementos: 100**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0007181680002759094 |
| Selección | 0.00044701600018015597 |
| MergeSort | 0.0004783710000992869 |
| Quicksort | 0.00024651199964864645 |
| Inserción | 0.0003629569991971948 |
**Cantidad de elementos: 500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.004909119999865652 |
| Selección | 0.0110821020007279 |
| MergeSort | 0.002761871000075189 |
| Quicksort | 0.001536663000479166 |
| Inserción | 0.010580675999335654 |
**Cantidad de elementos: 1000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.010790530999656767 |
| Selección | 0.04486219200043706 |
| MergeSort | 0.005838908999976411 |
| Quicksort | 0.003595244999814895 |
| Inserción | 0.0408951290000914 |
**Cantidad de elementos: 2000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.023730072000034852 |
| Selección | 0.17941214899929037 |
| MergeSort | 0.013341390000277897 |
| Quicksort | 0.007994433000021672 |
| Inserción | 0.16681694100043387 |
**Cantidad de elementos: 3000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.03778030900048179 |
| Selección | 0.40675585699955263 |
| MergeSort | 0.01893358300003456 |
| Quicksort | 0.011600621000070532 |
| Inserción | 0.3734729919997335 |
**Cantidad de elementos: 4000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.0521422950005217 |
| Selección | 0.7219909189998361 |
| MergeSort | 0.025806763999753457 |
| Quicksort | 0.01662027800011856 |
| Inserción | 0.6700706999999966 |
**Cantidad de elementos: 5000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.06700311599979614 |
| Selección | 1.1312324929995157 |
| MergeSort | 0.03276559100049781 |
| Quicksort | 0.02272750999964046 |
| Inserción | 1.049954611999965 |
**Cantidad de elementos: 7500**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.10514335199968627 |
| Selección | 2.5331957110001895 |
| MergeSort | 0.050633720999940124 |
| Quicksort | 0.030572489999940444 |
| Inserción | 2.352385174999654 |
**Cantidad de elementos: 10000**
| Algoritmo | Tiempo de ejecución (s) |
|-----------|-------------------------|
| Heapsort  | 0.14503365799919266 |
| Selección | 4.530564047000553 |
| MergeSort | 0.06854273199951422 |
| Quicksort | 0.042633024999304325 |
| Inserción | 4.252776483999696 |
d)
#### Tiempo medio con 50 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.0003298004807970045 |
| Selección | 0.00013083834977933861 |
| Mergesort | 0.00023580199998107787 |
| Quicksort | 0.00012194083406313894 |
| Inserción | 0.00010067983583716966 |
#### Tiempo medio con 100 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.0007247297246397721 |
| Selección | 0.0004486266798213734 |
| Mergesort | 0.00047982986346184475 |
| Quicksort | 0.0002497603338049714 |
| Inserción | 0.0003789045405540037 |
#### Tiempo medio con 500 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.004888808857476334 |
| Selección | 0.011094667812789893 |
| Mergesort | 0.002757735193334554 |
| Quicksort | 0.001501715076367205 |
| Inserción | 0.01042211682185723 |
#### Tiempo medio con 1000 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.01082875558189933 |
| Selección | 0.04502248397095876 |
| Mergesort | 0.00584529233796971 |
| Quicksort | 0.003506901652045258 |
| Inserción | 0.0409498724160553 |
#### Tiempo medio con 2000 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.02383555138088056 |
| Selección | 0.17983277715210022 |
| Mergesort | 0.012822466433798141 |
| Quicksort | 0.007783576734286868 |
| Inserción | 0.16681784541239786 |
#### Tiempo medio con 3000 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.037735805689562696 |
| Selección | 0.4071431871011413 |
| Mergesort | 0.01896053938660458 |
| Quicksort | 0.011680128970684933 |
| Inserción | 0.3761444555486815 |
#### Tiempo medio con 4000 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.05221940992985097 |
| Selección | 0.7219840037342387 |
| Mergesort | 0.026011349667937722 |
| Quicksort | 0.016142009466967977 |
| Inserción | 0.6706326836875611 |
#### Tiempo medio con 5000 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.06716955575572925 |
| Selección | 1.1285243604194548 |
| Mergesort | 0.032795204257913824 |
| Quicksort | 0.0222334473710184 |
| Inserción | 1.0522567008789494 |
#### Tiempo medio con 7500 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.10555483218916883 |
| Selección | 2.533056245873178 |
| Mergesort | 0.05055741457614715 |
| Quicksort | 0.03188779323241775 |
| Inserción | 2.3673165623728547 |
#### Tiempo medio con 10000 iteraciones:
| Algoritmo | Tiempo medio (seg) |
|-----------|--------------------|
| Heapsort  | 0.1456751018200908 |
| Selección | 4.51789061094763 |
| Mergesort | 0.06924800057395863 |
| Quicksort | 0.04411823011679061 |
| Inserción | 4.242444782562448 |
#### Gráfico para comparar todos los algoritmos con los tiempos medios
![alt text](https://github.com/MartinAndu/TDA1-1C2018/raw/master/tp1/todos_elementos.png)

#### Gráfico para comparar todos los algoritmos con los tiempos medios (excepto heapsort e Inserción )
![alt text](https://github.com/MartinAndu/TDA1-1C2018/raw/master/tp1/todos_elementos_excepto_insertion_selection.png)
