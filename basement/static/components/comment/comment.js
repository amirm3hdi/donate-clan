"use strict";

app.service("Comment", function (Account, Main, Auth, API, toaster, $rootScope) {
  return function (data) {

    /**
     * @private
     */
    var self = this;

    /**
     * @type {object}
     */
    this.get = data;

    /**
     * @type {Account}
     */
    this.user = data.user ? new Account(data.user) : null;

    /**
     * @type {string}
     */
    this.comment = this.get.comment;

    /**
     * @type {number}
     */
    this.kind = this.get.kind;

    /**
     * @type {string}
     */
    this.target = this.get.target;

    /**
     * Used for API calls
     *
     * @type {boolean}
     */
    this.loading = false;

    /**
     * @type {function}
     * @returns {boolean|null}
     */
    this.create = function () {
      this.loading = true;

      // Check auth
      if (!Auth.isAuth()) {
        toaster.error("Not signed in", "You need to sign in to comment.");
        return;
      }

      API.Comments.save({
          kind: this.kind,
          target: this.target,
          comment: this.comment
        },
        function (data) {
          toaster.success("Done", "Succesfully commented.");
          $rootScope.$broadcast("royalePlus.Comment:create", data);
          self.loading = false;
          self.comment = "";
        },
        function () {
          toaster.error("Ops", "Failed to comment, try again later.");
          self.loading = false;
        }
      );
    };
  };
});
