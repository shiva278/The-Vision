/*
    app.js is the server that handles :
    1)  routing
    2)  image & PDF file(s) upload
    3)  text-detection
*/

// ************************ INCLUDING REQUIRED MODULES ************************

var express = require('express')
var app = express()
var path = require('path')
var fs = require('fs')

app.set('view engine', 'ejs')

app.use(express.static(__dirname + '/public'))

var multer = require('multer');
const { type } = require('os');
var upload = multer({dest: 'uploads/imgs/'})

var bodyParser = require('body-parser')

var jsonParser = bodyParser.json()

const pdfparse = require('pdf-parse')

var vision = require('@google-cloud/vision')

const client = new vision.ImageAnnotatorClient({
    keyFilename: './key.json'
});

// ************************ INCLUDING REQUIRED MODULES ************************

// ************************ DEFINING ROUTES ************************

app.get('/', function(req, res) {
    res.render('signin')
})

app.get('/signin', (req, res) => {
    res.render('signin');
});

app.get('/signup', (req, res) => {
    res.render('signup');
});

app.get('/accounts', (req, res) => {
    res.render('accounts');
});

app.get('/forgetPass', (req, res) => {
    res.render('forgetPass');
});

app.get('/home', (req, res) => {
    res.render('home');
});

app.get('/mybooks', (req, res) => {
    res.render('mybooks');
});

app.get('/allbooks', (req, res) => {
    res.render('allbooks');
});

app.get('/book', (req, res) => {
    res.render('book', {bookname: req.query.bookname});
});

app.get('/image', (req, res) => {
    res.render('image');
});

app.get('/pdf', (req, res) => {
    res.render('pdf');
});

// ************************ DEFINING ROUTES ************************

// ************************ MULTIPLE IMAGE UPLOAD & TEXT-DETECTION ************************

    app.post('/up_multiple', upload.array('files'), function(req, res, next) {

        var detected_text = []

    // ************************ STORING IMAGE FILE PATHS IN "file_paths" ARRAY ************************

        var file_paths = req.files.map(function(file) {
            return file.path
        })

    // ************************ STORING IMAGE FILE PATHS IN "file_paths" ARRAY ************************

    // PERFORMING TEXT-DETECTION ON EACH OF THE IMAGE FILES AND RETURNING A PROMISE
        var promises = file_paths.map(async function(pic){
            
            const [result] = await client.textDetection(pic)
            const texts = result.fullTextAnnotation;
            var text_promise = texts.text
            return text_promise
        })

    // PERFORMING TEXT-DETECTION ON EACH OF THE IMAGE FILES AND RETURNING A PROMISE

    // IF PROMISE IS RESOLVED, DETECTED-TEXT IS SENT TO CLIENT-SIDE ELSE ERROR IS SENT

        Promise.all(promises).then(results => {
            res.send(results)
        }).catch(err => {
            res.status(500).send(err)
        })

    })
    
    // IF PROMISE IS RESOLVED, DETECTED-TEXT IS SENT TO CLIENT-SIDE ELSE ERROR IS SENT

// ************************ MULTIPLE IMAGE UPLOAD & TEXT-DETECTION ************************

// ************************ SINGLE IMAGE UPLOAD & TEXT-DETECTION ************************
    
    app.post('/up_single', upload.single('file'), function(req, res, next) {
        client.textDetection(req.file.path).then(results => {
            res.send(results)
        }).catch(err => {
            res.status(500).send(err)
        })

    })
// ************************ SINGLE IMAGE UPLOAD & TEXT-DETECTION ************************

// ************************ PDFs UPLOAD & TEXT-DETECTION ************************
    app.post('/up_pdf', upload.single('file'), function(req, res, next) {
    
    // ************************ STORING PDF FILE PATH IN "pdfFile" ************************

        const file = req.file
        if (!file) {
          const error = new Error('Please upload a file')
          error.httpStatusCode = 400
          return next(error)
        }

        const pdfFile = fs.readFileSync(file.path)
    
    // ************************ STORING PDF FILE PATH IN "pdfFile" ************************

    // PERFORMING TEXT-DETECTION ON THE PDF FILE AND RETURNING DETECTED-TEXT ON SUCCESS ELSE ERROR IS RETURNED

        pdfparse(pdfFile).then(function (data) {
            res.send(data)
        }).catch(err => {
          res.status(500).send(err)
        })
      })

    // PERFORMING TEXT-DETECTION ON THE PDF FILE AND RETURNING DETECTED-TEXT ON SUCCESS ELSE ERROR IS RETURNED

// ************************ PDFs UPLOAD & TEXT-DETECTION ************************

// ************************ STARTING THE SERVER WHICH LISTENS AT PORT 3000 ************************

app.listen(3000)

// ************************ STARTING THE SERVER WHICH LISTENS AT PORT 3000 ************************
