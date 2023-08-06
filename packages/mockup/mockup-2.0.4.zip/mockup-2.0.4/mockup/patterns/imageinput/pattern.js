/* global define, portal_url, google, alert, $ */
/* jshint strict: false */


define([
  'jquery',
  'react',
  'imagesloaded',
  'mockup-patterns-base',
  'jcrop'
], function($, R, imagesLoaded, Base){
  'use strict';

  var D = R.DOM;

  var ImageEditor = R.createClass({
    getDefaultProps: function(){
      return {
        jcrop: null,
        coord: null
      };
    },

    getInitialState: function(){
      return {
        showLoading: false
      };
    },

    componentDidMount: function(){
      var self = this;
      self.addCropper();      
    },

    cropClicked: function(e){
      var self = this;
      e.preventDefault();
      var $img = $(self.refs.image.getDOMNode());
      self.removeCropper();
      self.setState({
        showLoading: true
      });
      $.ajax({
        url: self.props.parent.getUploadUrl(),
        dataType: 'json',
        type: 'POST',
        data: {
          action: 'crop',
          code: self.props.code,
          coord: JSON.stringify(self.props.coord),
          width: $img.width(),
          height: $img.height()
        },
        success: function(data){
          if(data.success){
            self.setState({
              showLoading: false
            });
          }
          setTimeout(function(){
            self.reloadCropper();
          }, 200);
        },
        error: function(){
          alert('An error happened cropping image');
          self.setState({
            showLoading: false
          });
          setTimeout(function(){
            self.reloadCropper();
          }, 200);
        }
      });
    },

    addCropper: function(){
      var self = this;
      if(!self.refs.image){
        return;
      }
      // need to know if dialog is shown yet, otherwise, wait until it is
      var $modal = $(self.props.parent.getDOMNode());
      if($modal.hasClass('in')){
        self._addCropper();
      }else{
        $modal.on('shown.bs.modal', function(){ 
          self._addCropper();
        });
      }
    },

    _addCropper: function(){
      var self = this;
      var $img = $(self.refs.image.getDOMNode());
      imagesLoaded($img, function(){
        self.props.checkSize(self);
        $img.Jcrop({
          aspectRatio: 5/4,
          onChange: function(c){
            self.props.coord = c;
          }
        }, function(){
          self.props.jcrop = this;
          this.editor = self;
          self.props.jcrop.setOptions({
            setSelect: [0, 0, 99999999, 99999999]
          });
        });
      });
    },

    removeCropper: function(){
      var self = this;
      if(self.props.jcrop !== undefined){
        self.props.jcrop.destroy();
      }
    },

    reloadCropper: function(){
      var self = this;
      self.removeCropper();
      if(self.refs.image){
        var $img = $(self.refs.image.getDOMNode());
        $img.attr('style', 'max-width: 100%; max-height: 400px');
        self.addCropper();
      }
    },

    getImageUrl: function(){
      return this.props.baseImageUrl + 'tmp_' + this.props.code + '?' + Math.floor(Math.random()*99999999999);
    },

    render: function(){
      var self = this;

      var body = [];
      var disabled = false;
      if(self.state.showLoading){
        disabled = true;
        body = [D.div({ className: 'progress-bar progress-bar-warning progress-striped active',
                        style: { width: '100%' } }, D.span({}, 'Cropping..'))];
      }else{
        body = [D.div({ className: 'clearfix' }, [
          D.img({ ref: 'image', src: self.getImageUrl(), style: { 'max-width': '100%', 'max-height': '400px' } })
        ])];
      }
      return D.div({}, [
        D.div({ className: 'alert alert-warning clearfix' }, [
          D.strong({}, 'Crop first'),
          ': Images need to be cropped to a proper dimension before they can be added. Click the crop button when done.',
          D.button({ className: 'btn btn-default pull-right', disabled: disabled, onClick: self.cropClicked }, 'Crop'),
        ])
      ].concat(body));
    }
  });

  var TmpFileUploadMixin = {
    getDefaultProps: function(){
      return {
        title: 'Add',
        edit: null,
        data: this.getDefaultData(),
        autoUpload: true
      };
    },

    getInitialState: function(){
      return {
        uploading: false,
        progress: null,
        canAdd: undefined
      };
    },

    buttonClickedHandler: function(e){
      e.preventDefault();
      if(this.props.edit !== null){
        this.buttonClickedOnEdit();
      }else {
        this.buttonClickedOnAdd();
      }
      this.props.parent.setState({
        showDialog: false,
        edit: null
      });
    },

    fileSelected: function(){
      if(this.props.autoUpload){
        this.uploadFile();
      }
    },

    uploadFile: function(){
      var self = this;
      var $el = $(self.refs.upload.getDOMNode());
      $el.wrap('<form enctype="multipart/form-data" action="' + self.getUploadUrl() + '" method="POST" />');
      var $form = $el.parent();
      $form.ajaxSubmit({
        dataType: 'json',
        data: self.getUploadData && self.getUploadData() || {},
        beforeSubmit: function(){
          self.setState({
            uploading: true,
            progress: 0
          });
        },
        uploadProgress: function(e, position, total, percentComplete){
          self.setState({
            progress: percentComplete
          });
        },
        success: function(data){
          $el.unwrap();
          if(data.success){
            self.fileUploaded(data);
            self.props.data = data.data;
            self.props.data.filename = $el.attr('value').split(/(\\|\/)/g).pop();
            self.setState({
              uploading: false,
              progress: 0
            });
          }else{
            if(data.msg){
              alert(data.msg);
            }else{
              alert('Unknown error uploading');
            }
            self.props.parent.setState({
              showDialog: false
            });
          }
        }
      });
    },

    render: function(){
      var additional = [];
      if(this.state.uploading){
        var width = '100%';
        var text = 'uploading';
        if(this.state.progress !== null){
          width = this.state.progress + '%';
          if(this.state.progress === 100){
            text = 'Finishing...';
          }else{
            text = width;
          }
        }
        additional.push(D.div({ className: 'progress' }, [
          D.div({ className: 'progress-bar progress-bar-warning progress-striped active',
                  style: { width: width } }, D.span({}, text))
        ]));
      }
      additional = additional.concat(this.renderBelowUpload());

      var upload = '';
      if(this.props.edit === null && !this.props.data.filename) {
        upload = D.div({ className: 'form-group' }, [
          D.label({}, 'Upload'),
          D.input({ key: this.props.data.filename, ref: 'upload', type: 'file',
                    className: 'form-control', name: 'file', onChange: this.fileSelected })
        ]);
      }

      return [
        upload,
        D.div({}, additional),
        D.div({}, this.renderFooter())
      ];
    },

    renderFooter: function(){
      var disabled = true;
      var buttonText = 'Add';
      if(this.props.edit !== null) {
        buttonText = 'Edit';
        disabled = undefined;
      }else{
        if(this.state.canAdd){
          disabled = undefined;
        }
      }
      return [
        D.button({ ref: 'addButton', type: 'button', disabled: disabled, className: 'btn btn-primary',
                   onClick: this.buttonClickedHandler }, buttonText),
      ];
    }
  };

  var ImageWidget = R.createClass({
    /* Makes sure images uploaded are correct dimension */

    mixins: [TmpFileUploadMixin],
    
    buttonClickedOnEdit: function(){
      this.props.parent.state.data[this.props.edit].caption = $(this.refs.caption.getDOMNode()).attr('value');
    },

    buttonClickedOnAdd: function(){
      this.props.parent.insertImage($.extend({}, this.props.data, {
        caption: $(this.refs.caption.getDOMNode()).attr('value')
      }));
    },

    getUploadUrl: function(){
      return this.props.parent.props.imageManagerUrl;
    },

    getUploadData: function(){
      return {
        action: 'upload'
      };
    },

    getDefaultData: function(){
      return {
        filename: null,
        caption: '',
        code: -1
      };
    },

    fileUploaded: function(){

    },

    renderBelowUpload: function(){
      var self = this;
      if(!self.state.uploading && self.props.data.code !== -1 && self.props.data.code !== undefined){
        return [ImageEditor({ code: self.props.data.code, parent: self,
                              baseImageUrl: self.props.parent.props.baseTmpImageUrl,
                              checkSize: function(ed){
                                // enable add button if right dimensions after crop
                                var $img = $(ed.refs.image.getDOMNode());
                                var width = $img.width(), height = $img.height();
                                // check for aspect ratio range
                                var ideal_height = Math.round(width / 1.25);
                                if(height >= (ideal_height - 3) && height <= (ideal_height + 3)){
                                  self.setState({
                                    canAdd: true
                                  });
                                }
                              } })];
      }else if(self.props.data.id) {
        // show larger image
        return [D.div({ className: 'preview-image-container' }, [
          D.img({ src: self.props.parent.props.baseImageUrl + self.props.data.id + '_preview'})
        ])];
      }
      return [];
    }

  });

  var Pattern = Base.extend({
    /*
      let's try a pattern following a
      react-like design pattern */
    name: 'imageinput',
    trigger: '.pat-imageinput',
    options: {},
    state: {},
    init: function(){
      debugger;
      this.$el.wrap('<div />');
      this.$el = this.$el.parent();
      this.render();
      this.componentDidMount();
    },
    render: function(){
      /* only called once */
    },
    update: function(){
      /* we don't have a shadow DOM
         so we do update instead */
    },
    setState: function(state){
      this.state = $.extend({}, state);
      this.update();
    }
  });

  return Pattern;
});
