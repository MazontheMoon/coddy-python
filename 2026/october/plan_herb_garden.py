def plan_herb_garden(plot_size, volunteers, include_rare):
    space_per_volunteer = plot_size / volunteers
    rare_herbs_status = "Yes" if include_rare else "No"
    return f"Each volunteer gets {space_per_volunteer} square meters. Rare herbs: {rare_herbs_status}"