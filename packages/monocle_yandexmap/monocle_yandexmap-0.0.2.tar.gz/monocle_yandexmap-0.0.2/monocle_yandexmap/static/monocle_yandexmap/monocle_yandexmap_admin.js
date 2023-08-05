$(document).ready(function(){

    $("input.location_picker").each(function (i) {
        var map = document.createElement('div');
        map.className = "location_picker_map";
        map.id = 'YMapsID';
        this.parentNode.insertBefore(map, this);
        $(this).css('display', 'none');


        var lat = 55.950161;
        var lng = -3.187408;
        if (this.value.split(',').length == 2) {
            values = this.value.split(',');
            lat = values[0];
            lng = values[1];
        }

        var map, geoPlacemark;

        YMaps.jQuery(function () {
            map = new YMaps.Map(YMaps.jQuery("#YMapsID")[0]); // Создаём карту.
            geoPlacemark = new YMaps.Placemark(new YMaps.GeoPoint(lat, lng), {draggable: 1}); // Создаём маркер.

            map.setCenter(new YMaps.GeoPoint(lat, lng), 10); // Задаём центр карты.
            map.addControl(new YMaps.SmallZoom()); // Добавляем на карту элемент управления SmallZoom.
            map.addOverlay(geoPlacemark); // Добавляе на карту маркер.

            YMaps.Events.observe(geoPlacemark, geoPlacemark.Events.Drag, function (obj) { // Обработчик события перетаскивания (drag) маркера.
                $('#id_map').val(obj.getGeoPoint()); // Присваиваем value объекта geopoint координаты маркера.
            });

            var search_element = '' +
            '<h3>Поиск по карте:</h3>' +
            '<input type="text" id="address" name="address">' +
            '<a id="ymap_search" href="#">Найти</a>';

            $('#YMapsID').after(search_element);

            $('#ymap_search').on('click', function(){
                showAddress(document.getElementById('address').value);
            })

        });

        function showAddress(value) { // Функция поиска.
            var geocoder = new YMaps.Geocoder(value, {results: 1, boundedBy: map.getBounds()}); // Делаем запрос к геокодеру.
            YMaps.Events.observe(geocoder, geocoder.Events.Load, function (obj) { // Обработчик события загрузки (load) данных геокодера.
                if (this.length()) { // Если есть результат...
                    geoCoords = obj.get(0).getGeoPoint(); // Координаты найденной точки.
                    geoPlacemark.setGeoPoint(geoCoords); // Задаём маркеру координаты найденной точки.
                    map.panTo(geoCoords); // Перемещаем карту к найденной точке.
                    $('#id_map').val(geoCoords); // Присваиваем value объекта geopoint координаты найденной точки.
                } else {
                    alert('Ничего не найдено!');
                }
            });
            YMaps.Events.observe(geocoder, geocoder.Events.Fault, function (geocoder, error) { // Обрабочик события ошибки (fault) запроса к геокодеру.
                alert("Произошла ошибка: " + error);
            });
        }

    });
});