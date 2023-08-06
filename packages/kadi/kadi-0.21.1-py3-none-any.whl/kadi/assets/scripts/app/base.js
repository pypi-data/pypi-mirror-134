/* Copyright 2020 Karlsruhe Institute of Technology
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License. */

import Visibility from 'visibilityjs';

import BroadcastMessage from 'scripts/lib/components/base/BroadcastMessage.vue';
import NotificationAlert from 'scripts/lib/components/base/NotificationAlert.vue';
import NotificationToast from 'scripts/lib/components/base/NotificationToast.vue';
import QuickSearch from 'scripts/lib/components/base/QuickSearch.vue';

// Stop the logo animation once the site loaded and the current animation iteration finished.
const stopAnimation = () => [].forEach.call(document.querySelectorAll('.kadi-logo'), (el) => {
  el.style.animation = 'none';
});

[].forEach.call(document.querySelectorAll('.kadi-logo'), (el) => {
  el.addEventListener('animationiteration', stopAnimation);
  el.addEventListener('webkitAnimationIteration', stopAnimation);
});

// Scroll required inputs to a more sensible location, also taking different page layouts into account.
window.addEventListener('invalid', (e) => kadi.utils.scrollIntoView(e.target), true);

// Vue instance for handling global, short lived alerts.
const alertsVm = new Vue({
  el: '#notification-alerts',
  components: {
    NotificationAlert,
  },
  data: {
    alerts: [],
  },
  methods: {
    alert(message, options) {
      let _message = message;
      const settings = {
        request: null,
        type: 'danger',
        timeout: 5000,
        scrollTo: true,
        ...options,
      };

      if (settings.request !== null) {
        if (settings.request.status !== 0) {
          _message = `${message} (${settings.request.status})`;
        } else {
          return;
        }
      }

      this.alerts.push({
        id: kadi.utils.randomAlnum(),
        message: _message,
        type: settings.type,
        timeout: settings.timeout,
      });

      if (settings.scrollTo) {
        kadi.utils.scrollIntoView(this.$el, 'bottom');
      }
    },
  },
});

kadi.alert = alertsVm.alert;

if (kadi.globals.user_active) {
  // Register global keyboard shortcuts.
  const keyMapping = {
    'H': '',
    'R': 'records',
    'C': 'collections',
    'G': 'groups',
    'T': 'templates',
    'U': 'users',
  };

  window.addEventListener('keydown', (e) => {
    if (['INPUT', 'SELECT', 'TEXTAREA'].includes(e.target.tagName)) {
      return;
    }

    if (e.shiftKey && !e.ctrlKey && !e.altKey && !e.metaKey) {
      for (const [key, endpoint] of Object.entries(keyMapping)) {
        if (e.key === key) {
          e.preventDefault();
          window.location.href = `/${endpoint}`;
          return;
        }
      }
    }
  });

  // Vue instance for the quick search in the navigation bar.
  new Vue({
    el: '#quick-search',
    components: {
      QuickSearch,
    },
  });

  // Vue instance for the global broadcast message.
  new Vue({
    el: '#broadcast-message',
    components: {
      BroadcastMessage,
    },
  });

  // Vue instance for handling global, persistent notifications.
  const toastsVm = new Vue({
    el: '#notification-toasts',
    components: {
      NotificationToast,
    },
    data: {
      notifications: [],
      title: null,
    },
    methods: {
      getNotifications(scrollTo = true) {
        axios.get('/api/notifications')
          .then((response) => {
            this.notifications = response.data;

            const numNotifications = this.notifications.length;
            if (scrollTo && numNotifications > 0) {
              this.$nextTick(() => kadi.utils.scrollIntoView(this.$el, 'bottom'));
            }

            if (numNotifications > 0) {
              document.title = `(${numNotifications}) ${this.title}`;
            } else {
              document.title = this.title;
            }
          });
      },
    },
    mounted() {
      this.title = document.title;

      Visibility.every(5000, () => this.getNotifications(false));
      this.getNotifications(false);
    },
  });

  kadi.getNotifications = toastsVm.getNotifications;
}
