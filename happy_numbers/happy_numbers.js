var hn = function() {

	function checkHappiness(n) {
		var numbersHistoric = []
		var square = n;
		while (true) {
			square = sumOfSquareDigits(square);
			if (square == 1)
				return true;
			if (numbersHistoric.indexOf(square) != -1)
				return false;
			numbersHistoric.push(square);
		}
	}

	function sumOfSquareDigits(n) {
		var digits = (n + '').split('');
		var sum = 0;
		for (var i = 0; i < digits.length; i++) {
			sum += parseInt(digits[i]) * parseInt(digits[i]);
		}

		return sum;
	}

	return {
		checkHappiness : checkHappiness
	}
}

module.exports = hn();