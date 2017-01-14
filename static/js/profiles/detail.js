var app = new Vue({
  el: '#profile',
  data: {
    tweet: "@" + pageData.profile.handle + " ",
    isTweetModalVisible: true
  },
  methods: {
    openTweetModal: function() {
      this.isTweetModalVisible = true;
    },
    noop: function() {},
    closeTweetModal: function() {
      this.isTweetModalVisible = false;
    },
    getCharsLeft: function(tweet) {
      return 140 - tweet.length;
    },
    charsLeftClassGivenTweet: function(tweet) {
      if (this.getCharsLeft(tweet) < 0) {
        return "red";
      } else {
        return "";
      }
    }
  }
});