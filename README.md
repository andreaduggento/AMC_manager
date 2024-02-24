
# Physics Problems Database Documentation

This project uses CouchDB to store LaTeX-formatted physics problems. Each problem is stored as a document in CouchDB, designed to support multilingual content (Italian and English) and accommodate different formats (multiple choice and open-ended questions).

## Document Structure

Each document in the database follows this structure:

```json
{
  "_id": "unique_problem_id",
  "short_title": "Example Short Title",
  "long_title": "Example Long and Descriptive Title",
  "main_topic": "ExampleTopic",
  "topic_tags": ["tag1", "tag2"],
  "skill_tags": ["knowledge", "reasoning"],
  "target": ["triennali", "medicina"],
  "question": {
    "pre_latex": "Text before the LaTeX question.",
    "italian_latex": "LaTeX formatted question here in Italian.",
    "english_latex": "LaTeX formatted question here in English.",
    "image": "optional_image_url_or_attachment_id"
  },
  "solution": "LaTeX formatted solution here.",
  "format": ["multiple_choice", "open"],
  "AMC_correctchoice": {
    "italian": "Correct answer in Italian",
    "english": "Correct answer in English"
  },
  "AMC_wrongchoices": {
    "italian": ["Wrong answer A in Italian", "Wrong answer B in Italian", "Wrong answer C in Italian"],
    "english": ["Wrong answer A in English", "Wrong answer B in English", "Wrong answer C in English"]
  }
}
```

### Field Descriptions

- `_id`: A unique identifier for the document.
- `short_title`: A concise title for the problem.
- `long_title`: A more detailed title.
- `main_topic`: The primary topic of the problem.
- `topic_tags` and `skill_tags`: Arrays of tags for categorization.
- `target`: Intended audience or difficulty level.
- `question`: Contains LaTeX-formatted question text, with `pre_latex` for introductory text, and `image` for optional images.
- `solution`: LaTeX-formatted solution to the problem.
- `format`: Indicates if the problem is suitable for "multiple_choice", "open" format, or both.
- `AMC_correctchoice`: Contains the correct choice in both Italian and English.
- `AMC_wrongchoices`: Lists the wrong choices in both languages.

## Getting Started

### Prerequisites

- Install CouchDB on your system. Follow the official [CouchDB installation guide](https://docs.couchdb.org/en/stable/install/index.html).

### Setup

1. Start CouchDB and access the Fauxton web interface at `http://localhost:5984/_utils`.
2. Create a new database named `physics_problems`.
3. Use the provided document structure to insert new physics problems into the database.

## Inserting Documents

Documents can be inserted manually via the Fauxton interface or programmatically using scripts. See the `scripts` directory for examples on how to insert documents using Python.

## Contributing

Contributions to the database are welcome. Please ensure that any submitted problems adhere to the specified document structure and are correctly categorized and tagged.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
