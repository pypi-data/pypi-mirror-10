QUDB: Question Database
=======================

*Manage a database of questions and use it to generate assessments, e.g.
assignments, quizzes, and exams.*

*qudb* is a personal question bank for instructors that allows you to:

1. Keep track of your collection of questions for a given course.

2. Query your database for *terms*, *assessment types*, *assessments*,
   or *questions*. An *assessment* is a pair of a *term* and an
   *assessment type*.

   Example queries:

   -  In which assessments has a given question been used?
   -  What questions make up a given assessment?
   -  What questions have been used in a given term?
   -  What questions have been used in final exams across all terms?

3. Use a template to render an assessment document using its questions.

4. Distinguish between essay questions (default) and multiple-choice
   questions.

5. Use arbitrary additional variables in your templates, so you can use
   the same templates across courses, and use a *course name* variable.

Getting Started
---------------

1. Create a database:

   .. code:: shell

       qm init  # creates ./qu.db

   Use the ``-D`` (or ``--database``) option to specify the database
   file location.

2. Add questions:

   .. code:: shell

       qm add --term 151 --assessment-type quiz1 questions/chapter1/whats-your-name.tex
       qm add --term 151 --assessment-type quiz1 questions/chapter1/mcq/choose-a-month.tex

   Use the ``-Q`` (or ``--questions-directory``) to specify where to
   look for the question files. You can also specify a question's
   *points*, whether it's a *bonus* question, and its *order* in the
   assessment if you want to insert it somewhere in the middle.

3. Generate an assessment:

   .. code:: shell

       qm render --term 151 --assessment-type quiz1 --pdflatex quiz-template.tex

   The ``--pdflatex`` option assumes that your template is a LaTeX file,
   requires the ``pdflatex`` program, and generates a PDF. Without it,
   you get a rendered template.

   The ``--config`` option allows specifying additional arbitrary
   template variables using an ini-style configuration file.

Assumptions
-----------

-  One `SQLite <https://www.sqlite.org/>`__ database file per course.
-  Questions and templates are text files.
-  Templates are `Jinja2 <http://jinja.pocoo.org/>`__ templates.
-  Multiple choice questions have an ``/mcq/`` component in their paths.
-  Although it is not required, *qudb* works well with the
   `exam <https://www.ctan.org/pkg/exam>`__ LaTeX package.

License
-------

BSD (2-clause).


