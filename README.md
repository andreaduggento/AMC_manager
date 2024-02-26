
# Physics Problems Database Documentation

This project uses CouchDB to store and manage LaTeX-formatted physics problems
to be used with [Auto-Multiple-Choice software](https://www.auto-multiple-choice.net/). Each problem is stored as a
document in CouchDB, designed to support multilingual content (Italian and
English) and accommodate different formats (multiple choice and open-ended
questions).

## Document Structure

Each document in the database follows this structure:

```json
{
  "_id": "unique_problem_id",
  "group_id": "topic_group_number",
  "q_id": "topic_group_number_question_number",
  "short_title": "ShortTitle",
  "long_title": "Example Long and Descriptive Title",
  "main_topic": "ExampleTopic",
  "topic_tags": ["tag1", "tag2",...],
  "skill_tags": ["skill1", "skill2", ...],
  "target": ["intended_audience"],
  "question": {
    "pre_latex": "FP_variables_and_calculations",
    "italian_latex": "question_text_in_Italian",
    "english_latex": "question_text_in_English",
    "image": "optional_image_url_or_attachment_id"
  },
  "solution": {
    "italian": "solution_text_in_Italian",
    "english": "solution_text_in_English"
  },
  "format": ["question_format"],
  "AMC_correctchoice": {
    "italian": "correct_choice_in_Italian",
    "english": "correct_choice_in_English"
  },
  "AMC_wrongchoices": {
    "italian": ["Wrong answer A in Italian", "Wrong answer B in Italian", "Wrong answer C in Italian"],
    "english": ["Wrong answer A in English", "Wrong answer B in English", "Wrong answer C in English"]
  }
}
```

### Field Descriptions

- `_id`: Unique identifier for the document.
- `group_id`: Identifies the topic and group of the question.
- `q_id`: Unique identifier for the question within its group.
- `short_title`: A concise title for quick reference.
- `long_title`: A more detailed description of the problem.
- `main_topic`: The primary topic or concept the problem addresses.
- `topic_tags`: Keywords related to the problem's topics for easier searching and categorization.
- `skill_tags`: Keywords related to the skills or concepts tested by the problem (e.g., "knowledge", "reasoning")
- `target`: Intended audience or difficulty level of the problem (i.e., "medicine", "bacherlor").
- `question`: Contains the LaTeX-formatted question text, FP variables for dynamic content, and an optional image.
  - `pre_latex`: FP (Floating Point) calculations for dynamic question variables.
  - `italian_latex`/`english_latex`: Question text in Italian and English, respectively.
  - `image`: Optional URL or attachment ID for an image related to the problem.
- `solution`: Solution text in Italian and English, providing concise explanations or formulas.
- `format`: Indicates the question format (e.g., "multiple_choice", "open").
- `AMC_correctchoice`: The correct choice for multiple-choice questions, in both languages.
- `AMC_wrongchoices`: A list of plausible but incorrect choices for multiple-choice questions, in both languages.


### Suggested use of fields

- `group_id`: Used to group question which are similar, of which not more than one should not be drafted for any examination sheet. 
    - *XAbcd_gxxx* is the suggested format, where "XAbcd"  is a topic code (see list of topic codes below) and where xxx is a progressive number to indicated groups.
    - *q_id*: should identify the question within its group. Derived from group_id with an additional number: "XAbcd_gxxx_qyyy".


### Suggested taxonomy for topics

- `0Sgen`: general statistics
- `0Spro`: theory probability
- `0Sepi`: statistic concepts in epidemiology
- `1Pmat`: mathematics propaedeutics 
- `1Pvec`: vector algebra
- `1Puni`: units of measurements and convertion
- `1Pcin`: kinematics
- `2Mmec`: basic mechanics (forces, friction, equilibrium)
- `2Mene`: mechanics which involves the concept of energy 
- `2Mrot`: mechanics which involves the concept of torque
- `2Mela`: elasticity of materials, including springs 
- `3Ftor`: hydrostatic 
- `3Farc`: buoyant force
- `3Fcon`: fluid dynamics involving continuity princicple 
- `3Fber`: fluid dynamics involving Bernoulli principle
- `3Fpoi`: fluid dynamics involving Poiseuille principle 
- `3Fmem`: elastic membranes and capillary action
- `3Fcar`: topics in cardiovascular physics
- `4Ccal`: calorimetry
- `4Cdil`: thermal expansion
- `4Cter`: thermodynamics including 1st principle, kinetic theory of gases and ideal gas processes
- `5Esta`: electrostatic with electric field and electric potential
- `5Ecap`: electrostatic with electric field and electric potential
- `5Ecir`: electric circuits with batteries and resistors only
- `5Ecrc`: electric circuits with capacitors
- `5Ener`: nernst equilibrium
- `6Elor`: magnetism and Lorentz force
- `6Efar`: Faraday induction and Lentz principle
- `7Rdec`: radioactive decay
- `7Rdos`: dosimetry
- `7Rrad`: radiation physics 
- `7Rwav`: general principles about waves and electromagnetic waves
- `7Rsou`: mechanical waves and topics related to sound waves


## Getting Started

### Prerequisites

- Install CouchDB on your system. Follow the official [CouchDB installation guide](https://docs.couchdb.org/en/stable/install/index.html).

### Setup

1. Start CouchDB and access the Fauxton web interface at `http://localhost:5984/_utils`.
2. Create a new database named `AMC_01`.
3. Use the provided document structure to insert new physics problems into the database.

## Inserting Documents

Documents can be inserted manually via the Fauxton interface or programmatically using scripts. See the `scripts` directory for examples on how to insert documents using Python.

## Contributing

Contributions to the database are welcome. Please ensure that any submitted problems adhere to the specified document structure and are correctly categorized and tagged.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
