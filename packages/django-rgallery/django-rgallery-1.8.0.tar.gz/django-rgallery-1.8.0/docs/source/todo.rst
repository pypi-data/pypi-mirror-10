TODO
====

- √ Create documentation about installing rgallery in a django project from zero
- √ Static files + bower (here or in project, i.e. fontawesome for icons).
- √ Javascript in template (removeSelection(), ajaxChangeStatus()...).
- √ Copy metadata when photo is added via form.
- √ Test that photo uploads properly now that we're using Pillow instead PIL.
- √ Create custom commands documentation
- √ Add a button to allow select/deselect all the photos in the page.
- √ Add date and time to photo caption
- √ Add a site_base.html template as example
- √ Check that instructions are properly running by creating a project from zero
- √ Change THUMBNAIL_DEBUG = False to True (in project) and see why it's not
  properly uploading the photo.

- Activate folders via config.
- Check how myks-gallery makes the sync with a command and no signals
  - https://github.com/aaugustin/myks-gallery
  - https://github.com/aaugustin/myks-gallery/blob/master/gallery/admin.py
  - https://github.com/aaugustin/myks-gallery/blob/master/gallery/management/commands/scanphotos.py
- Change all prints to command.stdout.write() in commands
- Check cache (#expire_view_cache("app_gallery-gallery")).
  - Add config options
- Split as you can the template in minor files (_partials), it's more reusable.
- Title + Descriptions