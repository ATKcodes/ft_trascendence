// User.js
export default class User {
    player = 'Player1';
    token = '';
	profile_image = 'download.jpg';
	friendlist = [];
	language = 'EN';
	match_history_pong = [];
	match_history_tictactoe = [];
	loses_pong = 0;
	wins_pong = 0;
	loses_tictactoe = 0;
	wins_tictactoe = 0;
	winrate_pong = 0;
	winrate_tictactoe = 0;

	constructor(){}
	fillData(data){
		this.player = data.player;
		this.token = data.token;
		this.profile_image = data.profile_image;
		this.friendlist = data.friendlist;
		this.language = data.language;
		this.match_history_pong = data.match_history_pong;
		this.match_history_tictactoe = data.match_history_tictactoe;
		this.loses_pong = data.loses_pong;
		this.wins_pong = data.wins_pong;
		this.loses_tictactoe = data.loses_tictactoe;
		this.wins_tictactoe = data.wins_tictactoe;
		this.winrate_pong = data.winrate_pong;
		this.winrate_tictactoe = data.winrate_tictactoe;
	}
	resetData(){
		this.player = 'Player1';
		this.token = '';
		this.profile_image = 'download.jpg';
		this.friendlist = [];
		this.language = 'EN';
		this.match_history_pong = [];
		this.match_history_tictactoe = [];
		this.loses_pong = 0;
		this.wins_pong = 0;
		this.loses_tictactoe = 0;
		this.wins_tictactoe = 0;
		this.winrate_pong = 0;
		this.winrate_tictactoe = 0;
	}
}