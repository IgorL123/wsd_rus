/**
 * Печатание текста - Тиккер
 * @param {object} args
 */
function autotypingText( args ){

	let itemCount = Number( args.data.length )
	let curItemIndex = -1;
	let currentLength = 0;
	let theText = ''

	runTheTicker();

	function runTheTicker(){
		let theHold

		if( currentLength === 0 ){
			curItemIndex++;
			curItemIndex = curItemIndex % itemCount;
			theText = args.data[curItemIndex].text.replace( /"/g, '-' );
			args.element.href = args.data[curItemIndex].url;
		}

		args.element.innerHTML = theText.substring( 0, currentLength ) + znak();

		if( currentLength !== theText.length ){
			currentLength++;
			theHold = args.typingSpeed;
		}
		else{
			currentLength = 0;
			theHold = args.switchTimeout;
		}

		setTimeout( runTheTicker, theHold );
	}

	function znak(){
		return ( currentLength === theText.length ) ? '' : '|';
	}

}