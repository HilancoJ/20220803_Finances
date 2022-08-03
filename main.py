from website import create_app

app = create_app()

# Only execute this section if the main.py file is run. [https://www.youtube.com/watch?v=3dHyS1W4TIE&ab_channel=ProgrammingKnowledge]
if __name__ == '__main__':
	# debug=True means if there is a change in the code, it will automatically re-run the web server.
	app.run(debug=True, host="0.0.0.0")