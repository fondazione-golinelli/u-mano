<h1>U.MANO AR API</h1>

* Install miniconda Python 3.7 64 bit from https://docs.conda.io/en/latest/miniconda.html
* Once installed, open Anaconda Prompt

`> conda create -n umano python`

`> activate umano`

`(umano)> cd u-mano-ar-api`

`(umano)> pip install -r requirements.txt`

`(umano)> cd umanoar`

`(umano)> python manage.py migrate`

`(umano)> python manage.py loaddata dump\data.json`

`(umano)> python manage.py runserver`

Open a browser and go to http://localhost:8000

<h3>Site administration</h3>
* To edit/modify models create a super user in a shell

`(umano)> python manage.py createsuperuser`

then go to http://localhost:8000/admin/ and login


<h3> API</h3>
API at http://localhost:8000/api/artworks/

<h5>GET /api/artworks/ </h5>
<pre>
[
    {
        "uid": "QUADRO-01",
        "title": "Madonna col Bambino",
        "shader": {
            "parameters": [
                1.0,
                2.0,
                3.0,
                4.0,
                5.0,
                6.0
            ]
        },
        "nodes": [
            {
                "title": "a title",
                "mime": "txt/plain",
                "summary": "bla bla bla",
                "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nisl enim, vehicula at velit at, accumsan ornare mauris. Nunc lobortis id metus a bibendum. Aenean metus nulla, scelerisque imperdiet ligula quis, commodo aliquam leo. Maecenas laoreet purus lectus, quis euismod erat porttitor ut. Aenean lacinia, metus vel mattis ultrices, ipsum ante efficitur libero, vel ultrices enim felis ac arcu. Sed orci tellus, sollicitudin nec consectetur ac, varius sit amet sem. Integer dapibus, dolor eu ornare auctor, mauris lorem iaculis est, quis consectetur lorem nulla ut lectus. Pellentesque lobortis neque ante, quis vestibulum tortor pretium sit amet. Curabitur tristique nec ligula ut volutpat. Mauris tempor massa nec eros pharetra tincidunt. Nunc at nisi pharetra, aliquet purus at, varius risus.",
                "weight": 0.0,
                "url": null,
                "interactive": true
            },
            {
                "title": "a title 2",
                "mime": "txt/plain",
                "summary": "bla bla bla bla bla bla",
                "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nisl enim, vehicula at velit at, accumsan ornare mauris. Nunc lobortis id metus a bibendum. Aenean metus nulla, scelerisque imperdiet ligula quis, commodo aliquam leo. Maecenas laoreet purus lectus, quis euismod erat porttitor ut. Aenean lacinia, metus vel mattis ultrices, ipsum ante efficitur libero, vel ultrices enim felis ac arcu. Sed orci tellus, sollicitudin nec consectetur ac, varius sit amet sem. Integer dapibus, dolor eu ornare auctor, mauris lorem iaculis est, quis consectetur lorem nulla ut lectus. Pellentesque lobortis neque ante, quis vestibulum tortor pretium sit amet. Curabitur tristique nec ligula ut volutpat. Mauris tempor massa nec eros pharetra tincidunt. Nunc at nisi pharetra, aliquet purus at, varius risus.",
                "weight": 0.0,
                "url": null,
                "interactive": true
            },
            {
                "title": "an image",
                "mime": "image/jpeg",
                "summary": "non è quella vera",
                "body": "",
                "weight": 0.7,
                "url": "https://www.barberinicorsini.org/wp-content/uploads/2016/11/Corsini-Gentileschi-Madonna-col-Bambino-dettaglio.jpg",
                "interactive": true
            }
        ],
        "settings": {
            "chaos": 0.5
        }
    }
]
</pre>