# fast-api-ml-model

<br>

<p style="text-align:center">
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="200" > 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png" width="100" > 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/2560px-Pandas_logo.svg.png" width="200" >

</p>


<br><br><br>
<hr>
<h3> 
    Bu proje fastapi kullanılarak bir machine learning modelinin nasıl deploy edilebileceğini içermektedir.<br>
    Bu projede kullanılan ML modeli Telco Customer Churn verisi kullanılarak oluşturulmuştur.
    <br>
    <a href="https://www.kaggle.com/datasets/blastchar/telco-customer-churn">Dataset</a>


</h3>

<hr>
<br><br>

<h2>Projeyi yüklemek için</h2>


``` bash
git clone https://github.com/YigitAgalar/fast-api-model.git
```

<h2>Kullanım</h2>


<h3>Uygulamayı başlatmak için</h3>

<hr>
<h4> ❗❗ Proje dosyasının içinde olduğunuzdan emin olun</h4> <br>

``` bash
uvicorn main:app
```
<h4>Eğer değişiklik yapıyorsanız kayıt ettiğinizde tekrar çalışması için sonuna `--reload` ekleyebilirsiniz. </h4>
<br>

``` bash
uvicorn main:app --reload
```

<h2>Test</h2>


<h3>Unit testi çalıştırmak için</h3>

``` bash
python test.py
```

<br>
<h3>POST request göndermek için <a>request.ipynb</a> notebookunu veya Postmani kullanarak <a>http://127.0.0.1:8000/predict</a> Endpointine request gönderebilirsiniz </h3>


<h2>Kaynak</h2>
<a href="https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-with-fastapi-docker-and-github-actions-13374cbd638a"> Deploying ML Model </a>
