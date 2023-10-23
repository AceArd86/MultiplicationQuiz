import random, time, cmd


class Quiz(cmd.Cmd):
	intro = "Multiplication Quiz"

	questions = 10
	answers = 0
	for questions in range(1, 10):
		# Picks two random numbers
		num1 = random.randint(0, 9)
		num2 = random.randint(0, 9)
		prompt = input('#%s: %s x %s = ' % (questions, num1, num2))
	try:
		prompt = input('^%s$' % (num1 * num2))
	except TimeoutError:
		print('Out of time!')
		print([('.*', 'Incorrect!')], timeout=8, limit=3)
	else:
		# This block runs if no exceptions were raised in the try block.
		print('Correct!')
		answers += 1
		time.sleep(1)
		# Brief pause to let user see the result.
	print('Score: %s / %s' % (answers, questions))


Quiz().cmdloop()

