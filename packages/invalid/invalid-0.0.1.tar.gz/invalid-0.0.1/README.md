# invalid

A small Python library and wrapper around [pick](https://github.com/wong2/pick) to help remove the boilerplate around validating and processing command line input.

## Installation

```sh
pip install invalid
```

## Usage

```py
>>> from invalid import prompt
```

### Primitives

```py
>>> age_prompt = prompt.Int("age")
>>> age_prompt.prompt()
```

```
Enter age: s
Invalid age 's'
Enter age: 28
```

```py
28
```

### Lists

```py
>>> fruit_prompt = prompt.List(
...    "fruit",
...    ["apple", "banana", "orange"]
    )
>>> fruit_prompt.prompt()
```

```
Enter fruit:
-> apple
   banana
   orange
```

```py
'apple'
```

### ID to name mapping

```py
>>> fruit_prompt = prompt.List(
...     "fruit",
...     {
...         "A crunchy apple": "apple",
...         "A sweet banana": "banana",
...         "A juicy orange": "orange"
...     }
... )
>>> fruit_prompt.prompt()
```

```
Enter fruit:
-> A crunchy apple
   A sweet banana
   A juicy orange
```

```py
'apple'
```

### Custom validation

```py
>>> postcode_prompt = prompt.Text(
...     "postcode",
...     validate=lambda text: len(text) <= 5 and text.isnumeric()
... )
```

```
Enter postcode: 392838
Invalid postcode '392838'
Enter postcode: 0773
```

```py
'0773'
```

### Forms

```py
>>> form = prompt.Form({
...     "name": prompt.Text("your full name"),
...     "dob": prompt.Text("your date of birth"),
...     "number": prompt.Text(
...         "your favourite number between 1 - 10",
...         validate=lambda num: 1 <= num <= 10
...     )
... })
>>> form.execute()
```

```
Enter your full name: John Doe
Enter your date of birth: 2 July 1987
Enter your favourite number between 1 - 10: 3
```

```py
{'name': 'John Doe', 'date': '1987-07-02', 'number': 3}
```
