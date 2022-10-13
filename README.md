# lynda_django

## LinkedIn learning - Django Essential Course (smartnotes)

Things to consider:-
1. The /home_* paths are for reviewing the diffrent methods of creating views.
2. A propper home page need to be made.
3. (read, update, delete) views need to be edited to be more secure.

Things to remember:-
1. In **ListView** `context_object_name = "notes" # default: "note_list" or "object_list"`
2. In **DetailView** `context_object_name = "note" # default: "note" or "object"`
3. Two ways of adding extra context in the genetic views:
    ```python3
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = 'Create New'
        return context
    ```
    
    or
    
    ```python3
    extra_context = {'today': datetime.today()}
    ```
4. [Date formating](https://docs.djangoproject.com/en/4.1/ref/settings/#date-format) inside Django templates
    ```django
    <span>
        created at {{note.created|date:"SHORT_DATETIME_FORMAT"}}
    </span>
    ```
5. The [**ModelAdmin**](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#modeladmin-objects) object 
    ```python3
    class NotesAdmin(admin.ModelAdmin):
        list_display = ('title',)

    admin.site.register(models.Note, NotesAdmin)
    ```

