# Report on training 

## First plan comparative analysis 
<p align="justify">Dopo aver concluso le precedenti fasi di bussiness understanding, data understanding, data preparation abbiamo finalmente effettuato l'addestramento del modello di classificazione per il task multi-class che ci eravamo preposti dopo aver completato la fase di bussiness e data understanding. L'addestramento è stato ostico e sicuramente non ci aspettavamo dalle analisi iniziali che potesse risultare così complicato come si è riscontrato in corso di effettivo addestramento. Siamo partiti dal voler compiere un analisi comparativa che vedesse a comfronto un modello di classificazione basato su di un albero decisionale, un modello che si basasse sul framework Bayesiano e infine un modello di addestrato tramite il processo dell'ensemble learning, il quale prevede di addestrare più modelli e una volta addestrati utilizzare una funzione di aggregazione capace di sintetizzare i risultati riportati da questi modelli in un unico risultato finale. Quindi il piano di addestramento iniziale prevedeva un'analisi comparativa tra i seguenti 3 modelli:</p>


      1. Decision Tree model C4.5
      2. Gaussin Naive Bayes
      3. Random Forest
     
<p align="justify">Con questa idea di partezza abbia utilizzato python 3.0 e la libreria di scikitlearn per importare ed anadare ad addestrare i modelli sopra elencati. Le fasi inizialii di training non si sono concluse con successo i modelli addestrati riportavano scarsi risultati sicuramente risultati che non avrebbeero risolto il problema che ci siamo pre posti. Conseguentemente a risultati di performance scadenti abbiamo deciso di rielaborare il piano iniziale e per prima cosa ci siamo posti di analizzare il **lower bound** del problema, il quale è stato identificato con la moda. In seguito il nostro primo obiettivo è stato quello di riuscire a battere questo stimatore che risulta essere uno stimatore zero-effort che ci viene dato dalla teoria statistica e in seguito in caso di successo avvremmo cercato di definire un **uper bound** con il quale ci saremmo ritenuti soddisfatti per affrontare il problema di classificazione dello stato di fibrosi del frgato di pazienti affetti da HCV. </p>
<br></br>

## Second plan bit the mode estimator
<p align="justify">Dopo aver ridefinito il piano di addestramento e gli obiettivi che vogliamo estrarre da questa fase si è proceduto all'addestramento dei seguenti 18 modelli: </p>

    1. Decision Tree C4.5
    2. Gaussian Naive Bayes
    3. Multinomial Naive Bayes
    4. Bernoulli Naive Bayes
    5. Complement Naive Bayes
    6. Random Forest
    7. Extra Tree Classifier
    8. Ada Boost Classifier
    9. XGBoost Classifier
    10. Gradient Boosting Classifier
    11. Perceptron
    12. Multi Layer Perceptron
    13. Logistic Regression
    14. Ridge Classifier
    15. Linear Support Vector Machine
    16. NuSVC support vector machine con coefficiente nu
    17. SVC support vector machine con coefficiente c
    18. Sthocastic Gradient Descent Classifier

<p align="justify">Per ogni uno di questi modelli si è effettuato un addestramento sul dataset di partenza, per ottenere una baseline line del modello preso in considerazione rispetto al problema e in seguito abbiamo addestrato il modello fornendoli i dataset rielaborati a seguito delle ipotesi avanzate durante la data cleaning and reduction. Infine per ogni modello abbiamo eseguito un ottimizzazione sul processo della cross validation per trovare il k numero di fold che permettesse di migliorare l'accurancy del modello, tale processo è stato ripetuto andando ad incrementare il numero di test effettuati e ove non ci sono state limitazione con le risorce computazionali è stata effettuata un ottimizzazione con iterazioni su k incrementale da 2 a 30, 100 e 300. Non ci siamo spinti oltre 300 perchè non avrebbe avuto senso data la cardinalità del dataset a disposizione. Infine questo processo è stato utilizzato per selezionare i migliori modelli sui quali abbiamo effettuato un processo di ottimizzazione dei parametri ed una volta individuati tali parametri siamo passati all'addestramento finale di tali modeli con la loro conseguente valutazione.</p>


### Decision Tree C4.5 training
<p align="justify">L'addestramento iniziale dell'albero ha visto una prima tecnica sperimentale con la quale si è voluta valutare la differenza con l'approccio classico che vede la cross validation. In questo esperimento abbiamo diviso il dataset iniziale nelle 2 partizioni per effettuare train e test in particolare è stato scelto un una suddivisione 90:10 ovvero il 90% del dataset è stato dedicato al training set mentre il 10% è stato riservato per il test set. Il motivo di tale suddivisione contro le classiche suddivisioni 70:30, 75:25 o la più spinta 80:20 è dovuto al tipo di valutazione condotta infatti con il training set è stato effettuato un processo di cross validation con 10 fold questo significa che il 90% dell'intero data set è stato partizionato in 10 parti eque e per 10 volte è stato addestrato il modello che vedeva sempre un nuovo trainig set leggermente diverso e un nuovo test set infine su questi modelli è stata calcolata l'accurancy media ed è stata posta a confronto con un single shoot training effettuato con l'intero 90% che era stato usato per la cross validation, mentre per il test è stato usato il 10% che avevamo lascitao da parte. Questo approccio ci aha permesso di mettere a confronto la media della cross validation con un single training su un dataset più grande.In seguito si è utilizzato il classico metodo con una cross validation a 10 folds e questi sono i risultati ottenuti:</p>

<img src="../img/img_describing_results/tree_statistiche.png" alt="Descrizione dell'immagine" width="500" height="200">
<br></br>

<p align="justify">In seguito si sono effettuati dei test di addestramento e valutazione delle performace sul modello con i principali valori di fold usati nella cross validation presi dalla letteratura scientifica i quali hanno dato i seguenti risultati:</p>

<img src="../img/img_describing_results/Tree_stat_principali_folds.png" alt="Descrizione dell'immagine" width="500" height="300">
<br></br>

<p align="justify">Infine riportiamo i risultati ottenuti dall'ottimizzazione dei folds richiesti per la cross vaalidation:</p>

<img src="../img/img_describing_results/best_k_for_cross_val_on_tree30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/best_k_tree_cv100d.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/best_k_for_tree_cv300.png" alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion on Decision Tree
<p align="justify"></p>






## Training of model based on Bayesian framework
### Gaussian Naive Bayes
<p align="justify"></p>

<img src="../img/img_describing_results/GNB_statistiche.png"  alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/GNB_stat_principali_valori_fold.png" alt="Descrizione dell'immagine" width="500" height="300">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_GausB30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_GausB100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_GausB300.png" alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion on Gaussian Naive Bayes
<p align="justify">......</p>




### Multinomial Naive Bayes
<p align="justify"></p>

<img src="../img/img_describing_results/MNB_stat_principali_fold.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/MNB_main__folds.png" alt="Descrizione dell'immagine" width="500" height="300">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/MNB_best_cv30.png" alt="Descrizione dell'immagine" width="500" height="200">
   
<img src="../img/img_describing_results/MNB_best_cv100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/MNB_best_cv300.png" alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion on Multinomial Naive Bayes 
<p align="justify">........</p>




### Bernoulli Naive Bayes
<p align="justify"></p>

<img src="../img/img_describing_results/BerNB_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/BerNB_principal_fold.png" alt="Descrizione dell'immagine" width="500" height="300">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_BernuolliNB30.png" alt="Descrizione dell'immagine" width="500" height="200">
   
<img src="../img/img_describing_results/BK_CV_BernoulliNB100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_BernoulliNB300.png" alt="Descrizione dell'immagine" width="500" height="200">


### Complement Naive Bayes
<p align="justify"></p>
   
<img src="../img/img_describing_results/ComNB_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/COMNB_principla_fold.png" alt="Descrizione dell'immagine" width="500" height="300">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_ComplementNB30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_ComplementNB100.png" alt="Descrizione dell'immagine" width="500" height="200">
<p align="justify"></p>

<img src="../img/img_describing_results/BK_CV_ComplementNB300.png" alt="Descrizione dell'immagine" width="500" height="200">
<p align="justify"></p>


#### Conclusion on Complement Naive Bayes
<p align="justify">.......</p>
<br></br>

## Training of model based on ensemble learning
###  Ensemble model with Bagging strategy
#### Random Forest
<p align="justify"></p>

<img src="../img/img_describing_results/RanF_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/RanF_principal_fold.png" alt="Descrizione dell'immagine" width="500" height="300">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_RanFo30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_RandFo100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion on Random Forest

#### Extra Tree
<p align="justify"></p>

<img src="../img/img_describing_results/ExT_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/ExT_principal_fold.png" alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_ExtraTree30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_Et100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion on Extra Tree

### Ensemble model with Boosting strategy
#### Ada Boost
<p align="justify"></p>

<img src="../img/img_describing_results/AdaB_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/AdaB_principal_fold.png" alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_AdaB30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion on Ada Boost

#### XGBoost
<p align="justify"></p>

<img src="../img/img_describing_results/XGB_stats.png"  alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/XGB_principal_fold.png"  alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_XGBoost30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion on XGBoost

#### Gradient Boost Classifier
<p align="justify"></p>

<img src="../img/img_describing_results/GrBos_Stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/GrBos_principal_folds.png" alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_GradientBoost30.png"  alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion on Gradient Boost Classifier

13. Logistic Regression
    14. Ridge Classifier
    15. Linear Support Vector Machine
    16. NuSVC support vector machine con coefficiente nu
    17. SVC support vector machine con coefficiente c
    18. Sthocastic Gradient Descent Classifier


## Model based on regression
### Logistic Regression
<p align="justify"></p>

<img src="../img/img_describing_results/LR_stats%20.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/LR_principal_folds.png" alt="Descrizione dell'immagine" width="500" height="100">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_LinearReg30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_LinearRegr100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion 

### Ridge Regression
<p align="justify"></p>

<img src="../img/img_describing_results/RigR_stast.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/RigR_principal_fold.png" alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_RidgeRegres30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_RidgeRegr100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion 

## Model based on Support Vector Macchine
### Linear Support Vector Macchine
<p align="justify"></p>

<img src="../img/img_describing_results/LSVM_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/LSVM_principal_folds.png" alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_SVM30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion 

### Nu Support Vectort Macchine or coefficient Nu SVM
<p align="justify"></p>

<img src="../img/img_describing_results/NSVM_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/NSVM_principal_folds.png" alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_NuSVM30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_NuSVM100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion 

### Support Vector Macchine coefficient C
<p align="justify"></p>

<img src="../img/img_describing_results/CSVM_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/CSVM_principal_folds.png" alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_SVCcoefC30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_SVCcoefC100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

#### Conclusion 

## Model based on Gradient Descent
### Sthocastic Gradient Descent Classifier
<p align="justify"></p>

<img src="../img/img_describing_results/SGD_stats.png" alt="Descrizione dell'immagine" width="500" height="100">

<img src="../img/img_describing_results/SGD_principal_folds.png" alt="Descrizione dell'immagine" width="500" height="400">
<br></br>

<p align="justify">Riportiamo di seguito i grafici di ottimizzazione della cross validation che visualizzazano l'andamento dell'accurnacy rispetto al numero di fold effettuati:</p>

<img src="../img/img_describing_results/BK_CV_SthocasticGDC30.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../img/img_describing_results/BK_CV_SVCcoefC100.png" alt="Descrizione dell'immagine" width="500" height="200">

<img src="../ alt="Descrizione dell'immagine" width="500" height="200">

<p style='text-align: justify;'>Visualizziamo la situazione generale del nostro dataset dei patienti fibrotici per sesso:</p>
<img src="../ alt="Descrizione dell'immagine" width="500" height="200">
<p align="justify"></p>


<p align="justify"></p>

<p align="justify"></p>