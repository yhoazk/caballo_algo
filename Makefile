all: clean get_doc run

clean:
	@rm -rf doc.aux doc.pdf doc.log

run:
	@python ./caballo.py

get_doc:
	@pdflatex ./tex/doc.tex
