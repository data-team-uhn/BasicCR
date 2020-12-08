# BasicCR
Identifies terms within a text using basic (as opposed to deep-learning) techniques

## Installation

1. After installing *NeuralCR*, copy the files `basic_text_matcher.py` and
`basic_text_matcher_flask_loader.py` to the *NeuralCR* directory.

2. Edit the file `app.py` adding the lines `import basic_text_matcher` and
`import basic_text_matcher_flask_loader` to immediately below the line
`import ncrmodel_flask_loader`.

3. Register the basic model loader by adding the
line `MODEL_LOADERS['basic'] = basic_text_matcher_flask_loader.loadfromrequest`
to immediately below the line `MODEL_LOADERS['neural'] = ncrmodel_flask_loader.loadfromrequest`.

## Usage

- `NCRModel` interface conforming *BasicCR* models can be instantiated by calling
`basic_text_matcher.BasicTextMatcher(id_file, title_file)` where `id_file` is
the file path to a JSON file of an object that maps different names to a common
identifier, and `title_file` is the file path to a JSON file of an object that
maps these common identifers to their human readable names.

- If `app.py` is started with the `--allow_model_put` flag, *BasicCR* models can
be instantiated through the REST API by making a HTTP PUT request
to `/models/<new model name>` with the arguments of:
  - `model_type` = `basic`
  - `id_file` = same as above described `id_file` argument
  - `title_file` = same as above described `title_file` argument
