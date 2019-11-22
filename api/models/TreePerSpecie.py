from django.contrib import admin
from api.models.Tree import TreeSpecie, Tree


class TreeListFilter(admin.SimpleListFilter):
    """
    This filter is an example of how to combine two different Filters to work together.
    """
    # Human-readable title which will be displayed in the right admin sidebar just above the filter
    # options.
    title = 'Tree per specie'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'TreePerSpecie'

    # Custom attributes
    related_filter_parameter = 'tree__species__id__exact'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_questions = []
        queryset = Tree.objects.order_by('species_id')
        if self.related_filter_parameter in request.GET:
            queryset = queryset.filter(species_id=request.GET[self.related_filter_parameter])
        for TreePerSpecie in queryset:
            list_of_questions.append(
                (str(TreePerSpecie.age), TreePerSpecie.name)
            )
        return sorted(list_of_questions, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(tree_id=self.value())
        return queryset

class TreeAdmin(admin.ModelAdmin):
    list_filter = (TreeListFilter,)


class SpeciesListFilter(admin.SimpleListFilter):

    title = 'species'

    parameter_name = 'species'

    default_value = None

    def lookups(self, request, model_admin):
        list_of_species = []
        queryset = TreeSpecie.objects.all()
        for species in queryset:
            list_of_species.append(
                (str(species.commonname), species.sciname)
            )
        return sorted(list_of_species, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(species_id=self.value())
        return queryset

    def value(self):
        value = super(SpeciesListFilter, self).value()
        if value is None:
            if self.default_value is None:
                first_species = TreeSpecie.objects.order_by('name').first()
                value = None if first_species is None else first_species.id
                self.default_value = value
            else:
                value = self.default_value
        return str(value)