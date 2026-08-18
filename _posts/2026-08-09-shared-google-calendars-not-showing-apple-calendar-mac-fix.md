---
layout: post
title: "Shared Google Calendars Missing or Stuck in Apple Calendar? Here's the Hidden Fix"
description: "If a shared Google Calendar is missing from Apple Calendar on Mac, iPhone or iPad, or a shared calendar keeps showing up and sending alerts, Google's hidden Sync Settings page is probably the fix."
date: 2026-08-09T18:35:00-04:00
categories:
  - Technology
  - How-To
author: Ray Hollister
tags:
  - Google Calendar
  - Apple Calendar
  - macOS
  - iPhone
  - Gmail
  - Shared Calendars
  - Calendar Sync
image: /media/2026/08/shared-google-calendar-apple-calendar-syncselect-fix.png
image_alt: "A clean editorial illustration of two calendar apps connected by a glowing sync bridge, with hidden toggle switches controlling which shared calendars appear or disappear."
image_caption: "The fix is not in Apple Calendar. It is hiding in Google's calendar sync settings. (Generated with OpenAI image generation)"
image_description: "Editorial hero image showing a Mac-style calendar interface and a Google Calendar sync settings panel connected by a glowing bridge, centered on hidden sync toggles that control whether shared calendars appear in Apple Calendar."
reading-time: true
---

If a shared Google Calendar is not showing in Apple Calendar on your Mac, iPhone or iPad, or the opposite is happening and a shared Google Calendar suddenly appears in Apple Calendar with no obvious way to hide it, the fix is probably the same hidden Google page:

[https://calendar.google.com/calendar/u/0/syncselect](https://calendar.google.com/calendar/u/0/syncselect)

Open that link while signed in to the same Google account (Gmail or Google Workspace) you use in Apple Calendar. Check the calendars you want Apple Calendar to sync. Uncheck the calendars you do not want Apple Calendar to sync. Save the setting. Then quit and reopen Apple Calendar, or refresh the Google account on your device.

That is the fix.

This solves two equally frustrating problems:

- A shared Google Calendar shows up in Google Calendar, Gmail or the Google Calendar app, but not in Apple Calendar.
- A shared Google Calendar shows up in Apple Calendar even though you only wanted to reference it occasionally in Google Calendar.

The second problem matters just as much as the first. You might subscribe to your boss's calendar in Google Calendar so you can see conflicts while planning a meeting. That does not mean you want every one of her events sitting in Apple Calendar, triggering alerts, crowding your day view and making your phone feel like it joined someone else's job.

Without Google's Calendar Sync Settings page, Apple Calendar does not give you a clean way to make that shared Google calendar disappear from your Apple devices. The calendar may not be listed where you expect. The notification settings may not be obvious. Removing and re-adding your Google account is overkill. The useful switch is on Google's side.

And for reasons I still do not understand, I have never been able to find official documentation from Gmail, Google Calendar or Apple that explains this clearly.

## The Problem

There are really two versions of the same Google Calendar and Apple Calendar sync problem.

The first version is the missing-calendar problem:

Someone shares a Google Calendar with you. You accept the invitation. You can see the calendar at [calendar.google.com](https://calendar.google.com/). You may also see it in Gmail, on your iPhone or iPad, or in the Google Calendar app.

Then you open Apple Calendar on your Mac and it is just not there.

Your main Google calendar is there. Your other shared calendars are there. But the shared calendar you actually need is missing.

The second version is the stuck-calendar problem:

You add or subscribe to a shared Google Calendar because you need occasional visibility. Maybe it is your boss's calendar, a teammate's schedule, a family member's calendar, a conference room or a shared work calendar. In Google Calendar, that makes sense. You can show it when you need it and hide it when you do not.

Then it suddenly appears in Apple Calendar too.

Now your Mac, iPhone or iPad may show events you do not actually want in your personal calendar flow. Worse, Apple devices may start notifying you about calendar invites, meetings and reminders that are not yours. You wanted scheduling context, not another person's full calendar life pushed into your notifications.

Both problems are confusing because everything looks like it should already be manageable from Apple Calendar. Your Google account is connected. Calendar sync is turned on. The shared calendar exists. Your permissions are fine. You can see the calendar in Google's own interface.

The missing piece is that Google has a separate calendar sync selection setting for external calendar clients, including Apple's built-in Calendar app on macOS, iOS and iPadOS.

## The Fix: Use Google's Calendar Sync Settings Page

Use these steps when a shared Google Calendar is missing from Apple Calendar or when a shared Google Calendar is showing in Apple Calendar and you want to remove it from your Apple devices without deleting the share from Google Calendar.

1. Open this page in your browser:

   [https://calendar.google.com/calendar/u/0/syncselect](https://calendar.google.com/calendar/u/0/syncselect)

2. Make sure you are signed in to the Google account that is connected to Apple Calendar.

3. Find the shared calendar in the list.

4. To make the calendar appear in Apple Calendar, check the box next to it.

5. To hide the calendar from Apple Calendar, uncheck the box next to it.

6. Save the change.

7. Open Apple Calendar on your Mac, iPhone or iPad.

8. If the calendar list is hidden on Mac, choose **View > Show Calendar List**.

9. Quit and reopen Apple Calendar, or refresh the Google account if the change does not appear right away.

In most cases, this is enough. Checked calendars become available to Apple Calendar. Unchecked calendars stop syncing to Apple Calendar.

That means you can keep a shared calendar available in Google Calendar for planning and conflict-checking without forcing it into Apple Calendar or accepting all of its notifications on your Apple devices.

## Why This Works

Apple Calendar does not simply show every calendar your Google account can see. It syncs the calendars Google exposes to external calendar clients.

Google Calendar in the browser can show calendars that Apple Calendar does not automatically pull in. A shared calendar can be valid, accepted and visible in Google Calendar while still being excluded from the list of calendars Google makes available to Apple Calendar.

The reverse is also true. A calendar can be available to Apple Calendar because Google has it selected for sync, even if you only wanted that calendar as a sometimes-visible reference inside Google Calendar.

The `syncselect` page is where Google lets you choose which calendars sync to external calendar clients. It is not just a "make missing calendars appear" page. It is also the "stop syncing this shared calendar to Apple Calendar" page.

The maddening part is that this page is not obvious from the normal Google Calendar interface. It feels like a leftover utility page from an older era of Google Calendar syncing, but it still solves a very current problem.

## Example: Your Boss's Calendar Is Useful in Google Calendar but Annoying in Apple Calendar

This is the version of the problem that made me want to rewrite this article.

Say you subscribe to your boss's calendar in Google Calendar. You do not need to manage it. You do not need to live inside it. You just need to know whether she is free at 2:00 PM before you propose a meeting.

That shared calendar is useful in Google Calendar because you can turn it on while planning and turn it off afterward. It is scheduling context.

But if Google exposes that calendar to Apple Calendar, your Apple devices may treat it like part of your actual calendar setup. Events can clutter your day, appear in calendar widgets and trigger notifications for meetings you are not attending.

That is not a permission problem. It is not necessarily an Apple Calendar bug. It is a sync-selection problem.

Go to [calendar.google.com/calendar/u/0/syncselect](https://calendar.google.com/calendar/u/0/syncselect), uncheck that shared calendar, save and refresh Apple Calendar. You can still keep the calendar in Google Calendar for conflict-checking without letting it invade Apple Calendar.

## The Reddit Thread Where This Fix Was Buried

I found myself pointing people to this fix in a Reddit thread titled ["Shared Calendars not showing in native Mac Calendar app"](https://www.reddit.com/r/Office365/comments/yihtac/shared_calendars_not_showing_in_native_mac/).

The original post was about shared Microsoft 365 calendars not showing in the native Mac Calendar app, even though they appeared in Outlook Web App, Outlook desktop and Apple Calendar on iPhone and iPad. A few people suggested Apple Calendar's delegation settings, which can be the right answer for Exchange and Microsoft 365 accounts.

But buried in the thread was the answer that fixes a related and extremely common Google Calendar version of the same headache: Google's sync selection page.

I commented with the link because I had just found it and felt like I needed to go around spreading it like the gospel. Other people replied that it solved the problem for them too.

That is usually a sign that the fix is real, useful and poorly documented.

## What If This Is a Microsoft 365 or Exchange Calendar?

If the shared calendar is a Microsoft 365, Office 365, Outlook or Exchange shared calendar, the Google sync page is not the right fix.

For Microsoft 365 and Exchange calendars in Apple Calendar on Mac, check Apple Calendar's delegation settings instead:

1. Open Apple Calendar on your Mac.

2. Choose **Calendar > Settings**.

3. Click **Accounts**.

4. Select the Exchange or Microsoft 365 account.

5. Click **Delegation**.

6. Add or show the calendar account you have access to.

Apple's own Calendar User Guide documents this under [Share calendar accounts on Mac](https://support.apple.com/guide/calendar/share-calendar-accounts-icl27527/mac). Apple says delegated CalDAV accounts appear in the accounts you can access list, and for Exchange accounts you can add the person who gave you access, then select **Show** to display that delegated account's calendars.

So the short version is:

- Missing or unwanted shared Google Calendar in Apple Calendar: use Google's `syncselect` page.
- Missing or unwanted shared Microsoft 365 or Exchange calendar in Apple Calendar: check Apple Calendar's Delegation tab and account settings.

## Why I Am Writing This Down

I have never been able to find official documentation from Gmail, Google Calendar or Apple that explains this specific problem in a clear, searchable way:

> A shared Google Calendar can be visible in Google Calendar but missing from Apple Calendar, or visible in Apple Calendar when you do not want it there, and the fix is Google's hidden calendar sync settings page.

Google does have general help pages about syncing Google Calendar with Apple Calendar. That is useful as far as it goes, but it does not clearly surface the `syncselect` page as the control panel for shared calendars appearing in Apple Calendar.

Apple has documentation for sharing calendar accounts and seeing delegated calendar accounts on Mac, but that mostly explains Apple Calendar's side of CalDAV and Exchange delegation. It does not tell a Google Calendar user, in plain English, "Go to this Google URL and check or uncheck the shared calendar."

The result is a very modern support nightmare: the answer exists, but not where ordinary people would reasonably expect to find it.

## Quick Troubleshooting Checklist

If the shared calendar still does not behave after using the sync settings page, run through this checklist.

**Confirm the calendar is attached to the right Google account.**

Open Google Calendar in a browser and make sure the calendar appears while you are signed in to the same Gmail or Google Workspace account that is connected to Apple Calendar.

**Check Google's sync selection page again.**  
Go back to [calendar.google.com/calendar/u/0/syncselect](https://calendar.google.com/calendar/u/0/syncselect) and make sure the calendar is checked if you want it in Apple Calendar, or unchecked if you want it hidden from Apple Calendar.

**Show the calendar list in Apple Calendar.**  
In Apple Calendar on Mac, choose **View > Show Calendar List**. The calendar may be present but unchecked locally.

**Turn off alerts if you need a temporary workaround.**

If a shared calendar is still visible while you wait for sync to settle, check whether Apple Calendar lets you ignore alerts for that calendar or account. This is a workaround, not the real fix, because the cleaner solution is to stop syncing calendars you do not want on Apple devices.

**Refresh Apple Calendar.**  
Quit and reopen Calendar. You can also go to **Calendar > Settings > Accounts**, select the Google account and check its refresh settings.

**Check macOS Internet Accounts.**  
Open **System Settings > Internet Accounts**, select your Google account and make sure Calendars are enabled.

**Give it a few minutes.**  
Calendar sync is not always instant. If you have just changed the sync selection, wait a little, then reopen Apple Calendar.

**Remove and re-add the account only as a last resort.**  
This is the classic troubleshooting step everyone suggests because it feels decisive. It may work, but it should not be your first move. The sync selection page is faster and more targeted.

## FAQ

### Why is my shared Google Calendar not showing in Apple Calendar on Mac?

Usually because the calendar has not been selected on Google's Calendar Sync Settings page. Apple Calendar can only sync the Google calendars that Google exposes to external calendar clients.

### Why did a shared Google Calendar suddenly show up in Apple Calendar?

Because Google is exposing that calendar to external calendar clients for your account. Open [calendar.google.com/calendar/u/0/syncselect](https://calendar.google.com/calendar/u/0/syncselect), uncheck the shared calendar, save and refresh Apple Calendar.

### How do I remove my boss's shared Google Calendar from Apple Calendar without deleting it from Google Calendar?

Use Google's Calendar Sync Settings page. Uncheck your boss's calendar there. That should stop it from syncing into Apple Calendar while keeping it available in Google Calendar for planning and conflict-checking.

### What is the Google Calendar Sync Settings link?

The link is:

[https://calendar.google.com/calendar/u/0/syncselect](https://calendar.google.com/calendar/u/0/syncselect)

Use it while signed in to the Google account connected to Apple Calendar.

### Does this work for Gmail calendars?

Yes, if by "Gmail calendar" you mean a Google Calendar attached to a Gmail or Google Workspace account. The fix is the same: open Google's sync settings page, select or deselect the shared calendar, save, then refresh Apple Calendar.

### Does unchecking a calendar delete it?

No. Unchecking a calendar on the sync settings page should stop that calendar from syncing to external calendar clients such as Apple Calendar. It does not delete the calendar from Google Calendar and does not remove your access to it.

### Does this fix Microsoft 365 shared calendars on Mac?

No. Microsoft 365 and Exchange shared calendars use a different path. In Apple Calendar, check **Calendar > Settings > Accounts > [Exchange account] > Delegation**. Apple's support page on [sharing calendar accounts on Mac](https://support.apple.com/guide/calendar/share-calendar-accounts-icl27527/mac) covers that workflow.

### Why does the shared calendar show on iPhone but not Mac?

Different Apple devices and calendar clients may be using different sync paths, cached settings or account states. The important thing is that seeing the calendar on one device does not guarantee Google has enabled it for every external calendar sync target. The sync selection page is still worth checking.

### Is this an Apple problem or a Google problem?

Mostly Google, in my opinion. Apple Calendar can sync Google calendars, but Google controls which calendars are made available through its sync settings. The frustrating part is that Google does not make that setting easy to discover.

## The Short Answer

If a shared Google Calendar is missing from Apple Calendar, or a shared Google Calendar is stuck in Apple Calendar and you want it gone, open:

[https://calendar.google.com/calendar/u/0/syncselect](https://calendar.google.com/calendar/u/0/syncselect)

Check the calendars you want Apple Calendar to show. Uncheck the calendars you want Apple Calendar to hide. Save. Reopen Apple Calendar.

That is the answer I wish had been easy to find the first time.
