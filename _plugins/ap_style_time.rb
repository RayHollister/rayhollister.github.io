module Jekyll
  module APStyleTimeFilter
    def ap_style_time(date)
      if date.nil?
        return ""
      end

      formatted_date = date.strftime("%B %-d, %Y at ")
      hour_minute_format = date.strftime("%M") == "00" ? "%-I" : "%-I:%M"
      hour = date.strftime("%-I").to_i
      am_pm = date.strftime("%p")

      if hour == 12 && am_pm == "AM"
        formatted_time = "midnight"
      elsif hour == 12 && am_pm == "PM"
        formatted_time = "noon"
      else
        formatted_time = date.strftime("#{hour_minute_format}")
        am_pm = am_pm.gsub("AM", "a.m.").gsub("PM", "p.m.").downcase
        formatted_time += " " + am_pm
      end

      formatted_date + formatted_time
    end
  end
end

Liquid::Template.register_filter(Jekyll::APStyleTimeFilter)