const express = require('express');
const axios = require('axios');
const xml2js = require('xml2js');
const { response } = require('express');
const app = express();
const PORT = process.env.PORT || 8000;
//const SPRINGER_API_KEY = process.env.SPRINGER_API_KEY;
const NODE_ENV = process.env.NODE_ENV;
const spawn = require("child_process").spawn; 


//--TUTO---------SPAWN NORMAL 
//https://fr.acervolima.com/executez-un-script-python-a-partir-de-node-js-en-utilisant-la-methode-spawn-du-processus-enfant/

//--TUTO-----------SPAWN ASYNC POUR LA SYNCHRO AVEC LE FRONT
//https://www.npmjs.com/package/@expo/spawn-async



if (process.env.NODE_ENV !== 'production') {
    require('dotenv').config();
}

app.get('/', (req, res) => res.send('Hello World!'));


app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*"); // update to match the domain you will make the request from
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });


app.get('/results/:query', (req,res) => {
    const query = req.params.query;
    axios.get(`http://export.arxiv.org/api/query?search_query=all:${query}&max_results=10`)
    .then(response => {
        const xmlRes = response.data;

        xml2js.parseString(xmlRes, (err, result) => {
            if(err) {
                console.log(error);
            }
            console.log(typeof(result.feed.entry));
            res.status(200).json(result.feed.entry);
        });


    })
    .catch(error => {
        res.send(error);
        console.log(error);
    });
    //-------------CREATION DE SPAWN 
    const process = spawn('python',["./test.py", query] ); // Fonction faut lancer le bon python avec le json reçu 
  
    process.stdout.on('data', function(data) { 
        console.log(data.toString()); 
    } )

    // TO BE DONE 
 //-------------CREATE FUNCTION RE ORDER THE REPONS BY THE SCORE

 //-----------------FETCH THE DATA TO REPONSE 

    //------------------CHEMIN TEST ./test.py

});

// app.get('/springer/:keyword', (req, res) => {
//     const keyword = req.params.keyword;
//     console.log("hi ", keyword);
//     axios.get(`http://api.springernature.com/metadata/json?q=keyword:${keyword}&api_key=${SPRINGER_API_KEY}`)
//     .then(response => {
//         console.log(typeof(response.data));
//         // console.log(response);
//         res.status(200).json(response.data.records);
//     }).catch(error => {
//         res.send(error);
//         console.log(error);
//     });
// })


app.listen(PORT, () => {
    console.log(`Example app listening on port ${PORT}!`)
});
