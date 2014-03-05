var hn = require('./happy_numbers');

describe('happy number', function() {

	it('is happy', function() {
		expect(hn.checkHappiness(1)).toBe(true);
		expect(hn.checkHappiness(7)).toBe(true);
		expect(hn.checkHappiness(13)).toBe(true);
		expect(hn.checkHappiness(921)).toBe(true);
	});
	
	it('is unhappy', function() {
		expect(hn.checkHappiness(2)).toBe(false);
		expect(hn.checkHappiness(3)).toBe(false);
		expect(hn.checkHappiness(4)).toBe(false);
		expect(hn.checkHappiness(922)).toBe(false);
	});
});
