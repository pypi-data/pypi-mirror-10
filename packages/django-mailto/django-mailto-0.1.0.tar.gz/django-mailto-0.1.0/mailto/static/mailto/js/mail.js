var mail = mail || {};

(function (mail, $) {
    mail.Admin = {

        frame: undefined,
        cke: undefined,

        init: function () {
            this.frame = window.frames['html'];
            this.$form = $('form');

            $(this.frame).on('load', this.onFrameLoad(this));
            this.$form.on('submit', this.onSubmit(this));
            $('select[name="template"]', this.$form).on('change', this.onChangeTemplate(this));
        },

        save: function () {
            this.$form.trigger('submit');
        },

        saveContinue: function () {
            this.$form.append('<input type="hidden" name="_continue" value="" />');
            this.save();
        },

        onSubmit: function (self) {
            return function (e) {
                self.extractData();
            };
        },

        onFrameLoad: function (self) {
            return function (e) {
                self.ajdustFrameHeight();

                self.cke = self.frame.contentWindow.CKEDITOR;
                self.cke.on('instanceReady', self.onCKEReady(self));

                for (var i in self.cke.instances) {
                    self.cke.instances[i].on('change', self.onCKEInstanceChange(self));
                }
            };
        },

        onCKEReady: function (self) {
            return function (e) {
                self.ajdustFrameHeight();
            };
        },

        onCKEInstanceChange: function (self) {
            return function (e) {
                self.ajdustFrameHeight();
            };
        },

        onChangeTemplate: function (self) {
            return function (e) {
                if (confirm('Are you sure? All changes will be saved too.')) {
                    self.saveContinue();
                }
            };
        },

        extractData: function () {
            var data = {};
            $.each(this.frame.contentWindow.CKEDITOR.instances, function (k, v) {
                var d = v.getData();
                if (d && d.length > 0) {
                    data[k] = v.getData();
                }
            });
            if (data && data !== {}) {
                $('input[name=html]').val(JSON.stringify(data));
            }
        },

        ajdustFrameHeight: function () {
            var h = this.frame.contentWindow.document.body.offsetHeight
            $('iframe').height(h + 15);
        }

    };

    $(document).ready(function () {
        mail.Admin.init();
    });
})(mail, django.jQuery);