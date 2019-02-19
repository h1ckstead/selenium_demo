def test_site_navigation(main_page, expected_page_titles):
    menu_element = main_page.get_catalogue_element_by_name("Компьютеры")
    main_page.hover_and_click(menu_element, "Ноутбуки")
    assert main_page.title == expected_page_titles.get("notebooks")


def test_items_filtering(notebooks_page):
    notebooks_page.get_manufacturer_element_by_name("HP").click()
    notebooks_page.get_manufacturer_element_by_name("Dell").click()
    tooltip_value = notebooks_page.get_tooltip_value()
    notebooks_page.get_tooltip_search_button().click()
    filtered_value = notebooks_page.get_filtered_value()
    assert tooltip_value == filtered_value
